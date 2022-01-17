odoo.define('atum_pos_group_cash_in_out.CashMoveButton', function(require) {
	"use strict";

	const Registries = require('point_of_sale.Registries');
	const CashMoveButton = require('point_of_sale.CashMoveButton');
    const PosComponent = require('point_of_sale.PosComponent');
    const { _t } = require('web.core');
    var session = require('web.session');

	const BiCashMoveButton = (CashMoveButton) =>
		class extends CashMoveButton {
        async onClick() {
            const group_cash_in_out_pos = await session.user_has_group('atum_pos_group_cash_in_out.group_cash_in_out_pos');
            console.log("group_cash_in_out_pos ::> ",group_cash_in_out_pos)
                                if(group_cash_in_out_pos){
                                    const { confirmed, payload } = await this.showPopup('CashMovePopup');
            if (!confirmed) return;
            const { type, amount, reason } = payload;
            const translatedType = TRANSLATED_CASH_MOVE_TYPE[type];
            const formattedAmount = this.env.pos.format_currency(amount);
            if (!amount) {
                return this.showNotification(
                    _.str.sprintf(this.env._t('Cash in/out of %s is ignored.'), formattedAmount),
                    3000
                );
            }
            const extras = { formattedAmount, translatedType };
            await this.rpc({
                model: 'pos.session',
                method: 'try_cash_in_out',
                args: [[this.env.pos.pos_session.id], type, amount, reason, extras],
            });
            if (this.env.pos.proxy.printer) {
                const renderedReceipt = this.env.qweb.renderToString('point_of_sale.CashMoveReceipt', {
                    _receipt: this._getReceiptInfo({ ...payload, translatedType, formattedAmount }),
                });
                const printResult = await this.env.pos.proxy.printer.print_receipt(renderedReceipt);
                if (!printResult.successful) {
                    this.showPopup('ErrorPopup', { title: printResult.message.title, body: printResult.message.body });
                }
            }
            this.showNotification(
                _.str.sprintf(this.env._t('Successfully made a cash %s of %s.'), type, formattedAmount),
                3000
            );
                    }

                    else{
this.showPopup('ErrorPopup', { title: _t('Cash In/Out'), body: _t('You have no access to Cash In/Out') });
//                        self.gui.show_popup('error',{
//                            'title': _t('Discount restriction'),
//                            'body': _t('You have no access to discount'),
//                        });

                    }

        }

		};

	Registries.Component.extend(CashMoveButton, BiCashMoveButton);

	return CashMoveButton;

});

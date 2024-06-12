// Copyright (c) 2022, B & K Securities and contributors
// For license information, please see license.txt

frappe.ui.form.on('Market Investment', {
	buy_amount: function(frm){
        	//frm.set_value('net_investment',(frm.doc.buy_amount-frm.doc.sell_amount));
		frm.set_value('net_investment',(frm.doc.buy_amount-frm.doc.sell_amount));
    	},
	sell_amount: function(frm){
		frm.set_value('net_investment',(frm.doc.buy_amount-frm.doc.sell_amount));
	},
	onload: function(frm) {
		frm.set_query("test", function(){
			return {
					filters: { 'disabled': 0 }
			}
		});
	},
});


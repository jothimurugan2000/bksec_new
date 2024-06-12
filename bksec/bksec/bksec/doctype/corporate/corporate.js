// Copyright (c) 2020, B & K Securities and contributors
// For license information, please see license.txt

frappe.ui.form.on('Corporate', {
	before_save: function(frm) {
		frm.doc.model_path =  frm.doc.base_path + frm.doc.sector_folder + '\\' + frm.doc.file_name  + '.' + frm.doc.file_extension;
	}
});

/* eslint-disable */
// rename this file from _test_[name] to test_[name] to activate
// and remove above this line

QUnit.test("test: OCR Language", function (assert) {
	let done = assert.async();
	let random_code = frappe.utils.get_random(3);
	let random_lang = frappe.utils.get_random(2);

	// number of asserts
	assert.expect(1);

	frappe.run_serially([
		// insert a new OCR Language
		() => frappe.tests.make('OCR Language', [
			// values to be set
			{code: random_code, lang: random_lang}
		]),
		() => {
			assert.equal(cur_frm.doc.code, random_code);
			assert.equal(cur_frm.doc.lang, random_lang);
		},
		() => done()
	]);

});

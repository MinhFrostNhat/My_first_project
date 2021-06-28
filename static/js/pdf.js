function Export() {
	html2canvas(document.getElementById('table-products'), {
		onrendered: function (canvas) {
			var data = canvas.toDataURL();
			var docDefinition = {
				content: [{
					image: data,
					width: 525,
					height:150
				}]
			};
			pdfMake.createPdf(docDefinition).download("Table.pdf");
		}
	});
}
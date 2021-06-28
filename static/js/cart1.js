var shoppingCartItems = [];


$(document).ready(function () {

    if (sessionStorage["shopping-cart-items"] != null) {
        shoppingCartItems = JSON.parse(sessionStorage["shopping-cart-items"].toString());
    }


    displayShoppingCartItems();
});



$(".add-to-cart").click(function () {
    var button = $(this);
    var id = button.attr("id");
    var name = button.attr("data-name");
    var price = button.attr("data-price");
    var quantity = 1;


    var item = {
        id: id,
        name: name,
        price: price,
        quantity: quantity
    };

    var exists = false;
    if (shoppingCartItems.length > 0) {
        $.each(shoppingCartItems, function (index, value) {

            if (value.id == item.id) {
                value.quantity++;
                exists = true;
                return false;
            }
        });
    }


    if (!exists) {
        shoppingCartItems.push(item);
    }


    sessionStorage["shopping-cart-items"] = JSON.stringify(shoppingCartItems);

    displayShoppingCartItems();
});


$("#button-clear").click(function () {
    shoppingCartItems = [];
    sessionStorage["shopping-cart-items"] = JSON.stringify(shoppingCartItems);
    $("#table-products > tbody").html("");
});



function displayShoppingCartItems() {
    if (sessionStorage["shopping-cart-items"] != null) {
        shoppingCartItems = JSON.parse(sessionStorage["shopping-cart-items"].toString());

        $("#table-products > tbody").html("");

        $.each(shoppingCartItems, function (index, item) {
            var htmlString = "";
            htmlString += "<tr>";
            htmlString += "<td>" + item.id + "</td>";
            htmlString += "<td>" + item.name + "</td>";
            htmlString += "<td style='text-align: right'>" + item.price + "</td>";
            htmlString += "<td style='text-align: right'>" + item.quantity + "</td>";
            htmlString += "<td style='text-align: right'>" + item.price * item.quantity + "</td>";
                
            

            htmlString += "</tr>";
                
                
            


            
            $("#table-products > tbody:last").append(htmlString);
            var table = document.getElementById("table-products"), sumVal = 0;
            
	        for(var i = 1; i < table.rows.length; i++)
	        {
                sumVal = sumVal + parseInt(table.rows[i].cells[4].innerHTML);
                
	        }
                document.getElementById("val").innerHTML = "total (usd) = " + sumVal;
	            console.log(sumVal);
            
            
            var table = document.getElementById("table-products"), sumVal1 = 0;
            
            for(var i = 1; i < table.rows.length; i++)
            {
                sumVal1 = sumVal1 + parseInt(table.rows[i].cells[3].innerHTML);
                    
            }
                document.getElementById("val1").innerHTML = "total product = " + sumVal1;
                console.log(sumVal1);

           

        });
           
                
    }

$.fn.fileUploader = function (filesToUpload, sectionIdentifier) {
    var fileIdCounter = 0;
  
    this.closest(".files").change(function (evt) {
        var output = [];
  
        for (var i = 0; i < evt.target.files.length; i++) {
            fileIdCounter++;
            var file = evt.target.files[i];
            var fileId = sectionIdentifier + fileIdCounter;
  
            filesToUpload.push({
                id: fileId,
                file: file
            });
  
            var removeLink = "<a class=\"removeFile\" href=\"#\" data-fileid=\"" + fileId + "\">Remove</a>";
  
            output.push("<li><strong>", escape(file.name), "</strong> - ", file.size, " bytes. &nbsp; &nbsp; ", removeLink, "</li> ");
        };
  
        $(this).children(".fileList")
            .append(output.join(""));
  
        //reset the input to null - nice little chrome bug!
        evt.target.value = null;
    });
  
    $(this).on("click", ".removeFile", function (e) {
        e.preventDefault();
  
        var fileId = $(this).parent().children("a").data("fileid");
  
        // loop through the files array and check if the name of that file matches FileName
        // and get the index of the match
        for (var i = 0; i < filesToUpload.length; ++i) {
            if (filesToUpload[i].id === fileId)
                filesToUpload.splice(i, 1);
        }
  
        $(this).parent().remove();
    });
  
    this.clear = function () {
        for (var i = 0; i < filesToUpload.length; ++i) {
            if (filesToUpload[i].id.indexOf(sectionIdentifier) >= 0)
                filesToUpload.splice(i, 1);
        }
  
        $(this).children(".fileList").empty();
    }
  
    return this;
  };
  
  (function () {
    var filesToUpload = [];
  
    var files1Uploader = $("#files1").fileUploader(filesToUpload, "files1");
    var files2Uploader = $("#files2").fileUploader(filesToUpload, "files2");
    var files3Uploader = $("#files3").fileUploader(filesToUpload, "files3");
  
    $("#uploadBtn").click(function (e) {
        e.preventDefault();
  
        var formData = new FormData();
  
        for (var i = 0, len = filesToUpload.length; i < len; i++) {
            formData.append("files", filesToUpload[i].file);
        }
  
        $.ajax({
            url: "http://requestb.in/1k0dxvs1",
            data: formData,
            processData: false,
            contentType: false,
            type: "POST",
            success: function (data) {
                alert("DONE");
  
                files1Uploader.clear();
                files2Uploader.clear();
                files3Uploader.clear();
            },
            error: function (data) {
                alert("ERROR - " + data.responseText);
            }
        });
    });
  })()

}
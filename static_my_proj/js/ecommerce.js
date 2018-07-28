$(document).ready(function () {
    // Contact Form Handler

    var contactForm = $('.contact-form')
    var contactFormMethod = contactForm.attr("method")
    var contactFormEndpoint = contactForm.attr("action")


    function displaySubmitting(submitBtn, defaultText, doSubmit) {
        if (doSubmit) {
            submitBtn.addClass("disabled")
            submitBtn.html("<i class='fa fa-spin fa-spinner'></i>Sending...")
        }
        else {
            submitBtn.removeClass("disabled")
            submitBtn.html(defaultText)
        }

    }

    contactForm.submit(function (event) {
        event.preventDefault()
        var contactFormSubmitBtn = contactForm.find("[type='submit']")
        var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
        var contactFormData = contactForm.serialize()
        var thisForm = $(this)
        displaySubmitting(contactFormSubmitBtn, "", true)
        $.ajax({
            method: contactFormMethod,
            url: contactFormEndpoint,
            data: contactFormData,
            success: function (data) {
                contactForm[0].reset()
                $.alert({
                    title: 'Success!',
                    content: data.message,
                    theme: "modern"
                })
                setTimeout(function () {
                    displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
                }, 500)
            },
            error: function (error) {
                console.log(error.responseJSON)
                var jsonData = error.responseJSON
                var msg = ""
                $.each(jsonData, function (key, value) {
                    msg += key + ": " + value[0].message + "<br>"
                })
                $.alert({
                    title: 'OOPS!',
                    content: msg,
                    theme: "modern"
                })
                setTimeout(function () {
                    displaySubmitting(contactFormSubmitBtn, contactFormSubmitBtnTxt, false)
                }, 500)
            }
        })
    })

    // Auto Search
    var searchForm = $(".search-form")
    var searchInput = searchForm.find("[name='q']") // input name = 'q'
    var typingTimer;
    var searchBtn = searchForm.find("[type='submit']")
    // var typingInterval = 500 // 0.5 seconds
    searchInput.keyup(function (event) {
        // Keyup is for methods to be triggered when key is released
        clearTimeout(typingTimer)
        typingTimer = setTimeout(performSearch, 1000)
    })

    function displaySearching() {
        searchBtn.addClass("disabled")
        searchBtn.html("<i class='fa fa-spin fa-spinner'></i>Searching...")
    }

    function performSearch() {
        displaySearching()
        var query = searchInput.val();
        setTimeout(function () {
            window.location.href = '/search/?q=' + query;
        }, 1000)

    }

    // Cart + Add Products
    var productForm = $(".form-product-ajax")
    productForm.submit(function (event) {
        event.preventDefault();
        //console.log('Form is not sending')
        var thisForm = $(this) //referrring to only the current form instance
        var actionEndpoint = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();
        console.log(formData);
        // ajax call
        $.ajax({
            url: actionEndpoint,
            method: httpMethod,
            data: formData,
            success: function (data) {
                var submitSpan = thisForm.find(".submit-span")
                console.log("data");
                console.log(data);

                if (data.added) {

                    submitSpan.html("In Cart <button type='submit' class='btn btn-link'>Remove?</button>")

                }
                else {
                    submitSpan.html("<button type='submit' class='btn btn-success'>Add to cart</button>")
                }
                var navbarCount = $(".navbar-cart-count")
                navbarCount.text(data.cartItemCount)
                var currentPath = window.location.href
                if (currentPath.indexOf("cart") != -1) {
                    refreshCart()
                }

            },
            error: function (errorData) {
                $.alert({
                    title: 'OOPS!',
                    content: 'An error occurred!',
                    theme: "modern"
                })

            }
        })


    })

    function refreshCart() {

        // this is some function

        console.log("In currentPathnt cart")
        var cartTable = $(".cart-table")
        var cartBody = cartTable.find(".cart-body")
        // cartBody.html("<h1>Changed</h1>")
        var productRows = cartBody.find(".cart-product")
        var currenUrl = window.location.href


        var refreshCartUrl = '/api/cart/';
        var refreshCartMethod = "GET";
        var data = {};


        $.ajax({
            url: refreshCartUrl,
            method: refreshCartMethod,
            data: data,
            success: function (data) {
                // console.log("success");
                // console.log(data);
                var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
                if (data.products.length > 0) {
                    productRows.html("")
                    var i = data.products.length;
                    $.each(data.products, function (index, value) {
                        console.log(value)
                        var newCartItemRemove = hiddenCartItemRemoveForm.clone();
                        newCartItemRemove.css("display", "block");
                        // newCartItemRemove.removeClass("hidden-class")
                        newCartItemRemove.find('.cart-item-product-id').val(value.id)

                        cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" +
                            newCartItemRemove.html() + "</td><td>" + value.price + "</td>" + "</td></tr>")
                        --i;
                    })

                    cartBody.find(".cart-subtotal").text(data.subtotal)
                    cartBody.find(".cart-total").text(data.total)
                } else {
                    // Refreshing the page by setting the same url
                    window.location.href = currenUrl
                }
            },
            error: function (errorData) {
                $.alert({
                    title: 'OOPS!',
                    content: 'An error occurred!'
                })

            },
        })


    }
});
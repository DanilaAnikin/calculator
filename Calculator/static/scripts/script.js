

document.addEventListener("DOMContentLoaded", function (event) {
    let body = document.querySelector('body');
    let result = document.querySelector('#result');
    let input_html = document.querySelector('#input_html');
    let dark_mode_btn = document.querySelector('.dark_mode_btn');
    let clear = document.querySelector('#clear');
    let history = document.querySelector('#history');
    let equalTo = document.querySelector('#equalTo');
    let delete_single_num = document.querySelector('#delete_single_num');

    let Normal_btn = document.querySelectorAll('#Normal_btn');


    let initial_value = "";

    Normal_btn.forEach((Normal_btn, index) => {
        Normal_btn.addEventListener('click', function () {
            let text = this.innerHTML;
            initial_value += text;
            input_html.value = initial_value;
        });
    });

    /*equal to button action*/
    equalTo.addEventListener('click', function () {
        if (input_html.value != "") {
            history.innerHTML = input_html.value;

            if (dark_mode_status == false) {
                input_html.value = eval(input_html.value);
                initial_value = input_html.value;
            } else {
                input = input_html.value.replace("+", "%2B")

                var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function () {
                    if (this.readyState != 4) return;

                    if (this.status == 200) {
                        input_html.value = this.responseText
                        initial_value = input_html.value;
                    }
                };
                xhr.open('GET', "/calculate?input=" + input, true);
                xhr.send();
            }

        }
        else {
            alert('please enter any Number');
        }
        
    });


    /*dark_mode*/
    let dark_mode_status = false;
    dark_mode_btn.addEventListener('click', function () {
        body.classList.toggle('dark_mode_active');
        if (dark_mode_status == false) {
            this.innerHTML = '<i class="fa fa-sun-o" aria-hidden="true"></i>';
            equalTo.innerText = "Py solve";
            document.getElementById("input_html").style.color = "white";
            dark_mode_status = true;
        } else {
            this.innerHTML = '<i class="fa fa-moon-o" aria-hidden="true"></i>';
            equalTo.innerText = "JS solve";
            document.getElementById("input_html").style.color = "black";
            dark_mode_status = false;
        }
    });


    /*clear all number*/
    clear.addEventListener('click', function () {
        input_html.value = "";
        initial_value = "";
    });

    /*delete single number*/
    delete_single_num.addEventListener('click', function () {
        input_html.value = input_html.value.substring(0, input_html.value.length - 1);
        initial_value = input_html.value;
    });

});
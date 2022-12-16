/*

=========================================================
* Volt Pro - Premium Bootstrap 5 Dashboard
=========================================================

* Product Page: https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard
* Copyright 2021 Themesberg (https://www.themesberg.com)

* Designed and coded by https://themesberg.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. Please contact us to request a removal. Contact us if you want to remove it.

*/
// var answers = ["A", "C", "B"],
//     tot = answers.length;
// function getCheckedValue(radioName) {
//     var radios = document.getElementsByName(radioName);
//     for (var y = 0; y < radios.length; y++)
//         if (radios[y].checked) return radios[y].value;
// }
// function getScore() {
//     var score = 0;
//     for (var i = 0; i < tot; i++)
//         if (getCheckedValue("question" + i) === answers[i]) score += 1;
//     return score;
// }
// function returnScore() {
//     document.getElementById("myresults").innerHTML =
//         "Your score is " + getScore() + "/" + tot;
//     if (getScore() > 2) {
//         console.log("Bravo");
//     }
// }
// Array of all the questions and choices to populate the questions. This might be saved in some JSON file or a database and we would have to read the data in.
// var myQuestions = [
//     {
//       question: "1. Who the fuck killed Magellan?",
//       answers: {
//         a: 'Lapu Lapu ', b: 'Cardo Dalisay', c: '\nDarna'
//       },
//       correctAnswer: 'a'
//     },
//     {
//       question: "2. What is the longest fucking bridge found in the Philippines?",
//       answers: {
//         a: 'Philippine Brigde \n',
//         b: 'San Juanico Bridge \n',
//         c: 'South Luzon Expressway Bridge'
//       },
//       correctAnswer: 'c'
//     },
//     {
//         question: "3. It is considered as largest leaving mammal",
//         answers: {
//           a: 'Tamaraw \n', 
//           b: 'Elephant \n',
//           c: 'Lion'
//         },
//         correctAnswer: 'b'
//       }

//   ];
  
//   var quizContainer = document.getElementById('quiz');
//   var resultsContainer = document.getElementById('results');
//   var submitButton = document.getElementById('submit');
  
//   generateQuiz(myQuestions, quizContainer, resultsContainer, submitButton);
  
//   function generateQuiz(questions, quizContainer, resultsContainer, submitButton){
  
//     function showQuestions(questions, quizContainer){
//       // we'll need a place to store the output and the answer choices
//       var output = [];
//       var answers;
  
//       // for each question...
//       for(var i=0; i<questions.length; i++){
        
//         // first reset the list of answers
//         answers = [];
  
//         // for each available answer...
//         for(letter in questions[i].answers){
  
//           // ...add an html radio button
//           answers.push(
//             '<label>'
//               + '<input type="radio" name="question'+i+'" value="'+letter+'">'
//               + letter + ': '
//               + questions[i].answers[letter]
//             + '</label> <br>'
//           );
//         }
  
//         // add this question and its answers to the output
//         output.push(
//           '<div class="question">' + questions[i].question + '</div>'
//           + '<div class="answers">' + answers.join('') + '</div>'
//         );
//       }
  
//       // finally combine our output list into one string of html and put it on the page
//       quizContainer.innerHTML = output.join('');
//     }
  
  
//     function showResults(questions, quizContainer, resultsContainer){
      
//       // gather answer containers from our quiz
//       var answerContainers = quizContainer.querySelectorAll('.answers');
      
//       // keep track of user's answers
//       var userAnswer = '';
//       var numCorrect = 0;
      
//       // for each question...
//       for(var i=0; i<questions.length; i++){
  
//         // find selected answer
//         userAnswer = (answerContainers[i].querySelector('input[name=question'+i+']:checked')||{}).value;
        
//         // if answer is correct
//         if(userAnswer===questions[i].correctAnswer){
//           // add to the number of correct answers
//           numCorrect++;
          
//           // color the answers green
//           answerContainers[i].style.color = 'lightgreen';
//         }
//         // if answer is wrong or blank
//         else{
//           // color the answers red
//           answerContainers[i].style.color = 'red';
//         }
//       }
  
//       // show number of correct answers out of total
//       resultsContainer.innerHTML = numCorrect + ' out of ' + questions.length;
//     }
  
//     // show questions right away
//     showQuestions(questions, quizContainer);
    
//     // on submit, show results
//     submitButton.onclick = function(){
//       showResults(questions, quizContainer, resultsContainer);
//     }
  
//   }

// addmission
jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});
const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);
const form1 = {
  'Freshmen': 'Admission Requirements - Freshmen:\n 1. Form 138 (Original Copy of un-cancelled 4th year high school report card)\n 2. Copy of high school diploma\n 3. Certificate of Good Moral Character issued by H.S. Guidance Counselor /Principal\n 4. Certified true copy of Birth Certificate\n 5. Two 2"x2" colored photograph',
  'Transferee': 'Admission Requirements - Transferees: \n 1. Certificate of Transfer (Honorable Dismissal) Certified true copy of Grades\n 2. Two 2"x2" colored photographs\n 3. Certified true copy of Birth Certificate Certificate of Good Moral Character from the Dean /Administrator of the previous school',
}


document.addEventListener('DOMContentLoaded', () => {
  $$('.form1').forEach( (v, i) => {
    v.addEventListener('click', () => {
      const form1Title = v.innerText;
      const form1Info = form1[v.innerText];
      $('.msgbox').innerText = form1Info;
      //This Part can be replaced by an ajax call to lookup info from the server
      //You can use jQuery $.ajax(), or javascript fetch, or javascript XMLHttpRequest
      //(above listed from easiest to more difficult)
    });
  });
});

jQuery(document).ready(function(s) {
    s(".clickable-row").click(function() {
        window.location = s(this1).data("href");
    });
});
const s = document.querySelector.bind(document);
const ss = document.querySelectorAll.bind(document);
const form2 = {
  'Freshmen': 'Admission Requirements - Freshmen:\n 1. Filling out of the Graduate School Application Form \n 2. Original Transcript of Records (TOR) for evaluation purposes \n 3. Interview by the Dean of the Graduate School',
  'Transferee': 'Admission Requirements - Transferees: \n 1. Certificate of Transfer (Honorable Dismissal) \n ',
}

document.addEventListener('DOMContentLoaded', () => {
    ss('.form2').forEach( (v, i) => {
      v.addEventListener('click', () => {
        const form2Title = v.innerText;
        const form2Info = form2[v.innerText];
        s('.msgbox').innerText = form2Info;
        //This Part can be replaced by an ajax call to lookup info from the server
        //You can use jQuery $.ajax(), or javascript fetch, or javascript XMLHttpRequest
        //(above listed from easiest to more difficult)
      });
    });
  });


"use strict";
const d = document;
d.addEventListener("DOMContentLoaded", function(event) {

    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-primary me-3',
            cancelButton: 'btn btn-gray'
        },
        buttonsStyling: false
    });

    var themeSettingsEl = document.getElementById('theme-settings');
    var themeSettingsExpandEl = document.getElementById('theme-settings-expand');

    if(themeSettingsEl) {

        var themeSettingsCollapse = new bootstrap.Collapse(themeSettingsEl, {
            show: true,
            toggle: false
        });

        if (window.localStorage.getItem('settings_expanded') === 'true') {
            themeSettingsCollapse.show();
            themeSettingsExpandEl.classList.remove('show');
        } else {
            themeSettingsCollapse.hide();
            themeSettingsExpandEl.classList.add('show');
        }
        
        themeSettingsEl.addEventListener('hidden.bs.collapse', function () {
            themeSettingsExpandEl.classList.add('show');
            window.localStorage.setItem('settings_expanded', false);
        });

        themeSettingsExpandEl.addEventListener('click', function () {
            themeSettingsExpandEl.classList.remove('show');
            window.localStorage.setItem('settings_expanded', true);
            setTimeout(function() {
                themeSettingsCollapse.show();
            }, 300);
        });
    }

    // options
    const breakpoints = {
        sm: 540,
        md: 720,
        lg: 960,
        xl: 1140
    };

    var sidebar = document.getElementById('sidebarMenu')
    if(sidebar && d.body.clientWidth < breakpoints.lg) {
        sidebar.addEventListener('shown.bs.collapse', function () {
            document.querySelector('body').style.position = 'fixed';
        });
        sidebar.addEventListener('hidden.bs.collapse', function () {
            document.querySelector('body').style.position = 'relative';
        });
    }

    var iconNotifications = d.querySelector('.notification-bell');
    if (iconNotifications) {
        iconNotifications.addEventListener('shown.bs.dropdown', function () {
            iconNotifications.classList.remove('unread');
        });
    }

    [].slice.call(d.querySelectorAll('[data-background]')).map(function(el) {
        el.style.background = 'url(' + el.getAttribute('data-background') + ')';
    });

    [].slice.call(d.querySelectorAll('[data-background-lg]')).map(function(el) {
        if(document.body.clientWidth > breakpoints.lg) {
            el.style.background = 'url(' + el.getAttribute('data-background-lg') + ')';
        }
    });

    [].slice.call(d.querySelectorAll('[data-background-color]')).map(function(el) {
        el.style.background = 'url(' + el.getAttribute('data-background-color') + ')';
    });

    [].slice.call(d.querySelectorAll('[data-color]')).map(function(el) {
        el.style.color = 'url(' + el.getAttribute('data-color') + ')';
    });

    //Tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
    })


    // Popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
      return new bootstrap.Popover(popoverTriggerEl)
    })
    

    // Datepicker
    var datepickers = [].slice.call(d.querySelectorAll('[data-datepicker]'))
    var datepickersList = datepickers.map(function (el) {
        return new Datepicker(el, {
            buttonClass: 'btn'
          });
    })

    if(d.querySelector('.input-slider-container')) {
        [].slice.call(d.querySelectorAll('.input-slider-container')).map(function(el) {
            var slider = el.querySelector(':scope .input-slider');
            var sliderId = slider.getAttribute('id');
            var minValue = slider.getAttribute('data-range-value-min');
            var maxValue = slider.getAttribute('data-range-value-max');

            var sliderValue = el.querySelector(':scope .range-slider-value');
            var sliderValueId = sliderValue.getAttribute('id');
            var startValue = sliderValue.getAttribute('data-range-value-low');

            var c = d.getElementById(sliderId),
                id = d.getElementById(sliderValueId);

            noUiSlider.create(c, {
                start: [parseInt(startValue)],
                connect: [true, false],
                //step: 1000,
                range: {
                    'min': [parseInt(minValue)],
                    'max': [parseInt(maxValue)]
                }
            });
        });
    }

    if (d.getElementById('input-slider-range')) {
        var c = d.getElementById("input-slider-range"),
            low = d.getElementById("input-slider-range-value-low"),
            e = d.getElementById("input-slider-range-value-high"),
            f = [d, e];

        noUiSlider.create(c, {
            start: [parseInt(low.getAttribute('data-range-value-low')), parseInt(e.getAttribute('data-range-value-high'))],
            connect: !0,
            tooltips: true,
            range: {
                min: parseInt(c.getAttribute('data-range-value-min')),
                max: parseInt(c.getAttribute('data-range-value-max'))
            }
        }), c.noUiSlider.on("update", function (a, b) {
            f[b].textContent = a[b]
        });
    }

    //Chartist

    if(d.querySelector('.ct-chart-sales-value')) {
        //Chart 5
          new Chartist.Line('.ct-chart-sales-value', {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            series: [
                [0, 10, 30, 40, 80, 60, 100]
            ]
          }, {
            low: 0,
            showArea: true,
            fullWidth: true,
            plugins: [
              Chartist.plugins.tooltip()
            ],
            axisX: {
                // On the x-axis start means top and end means bottom
                position: 'end',
                showGrid: true
            },
            axisY: {
                // On the y-axis start means left and end means right
                showGrid: false,
                showLabel: false,
                labelInterpolationFnc: function(value) {
                    return '$' + (value / 1) + 'k';
                }
            }
        });
    }

    if(d.querySelector('.ct-chart-ranking')) {
        var chart = new Chartist.Bar('.ct-chart-ranking', {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
            series: [
              [1, 5, 2, 5, 4, 3],
              [2, 3, 4, 8, 1, 2],
            ]
          }, {
            low: 0,
            showArea: true,
            plugins: [
              Chartist.plugins.tooltip()
            ],
            axisX: {
                // On the x-axis start means top and end means bottom
                position: 'end'
            },
            axisY: {
                // On the y-axis start means left and end means right
                showGrid: false,
                showLabel: false,
                offset: 0
            }
            });
          
          chart.on('draw', function(data) {
            if(data.type === 'line' || data.type === 'area') {
              data.element.animate({
                d: {
                  begin: 2000 * data.index,
                  dur: 2000,
                  from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
                  to: data.path.clone().stringify(),
                  easing: Chartist.Svg.Easing.easeOutQuint
                }
              });
            }
        });
    }

    if(d.querySelector('.ct-chart-traffic-share')) {
        var data = {
            series: [70, 20, 10]
          };
          
          var sum = function(a, b) { return a + b };
          
          new Chartist.Pie('.ct-chart-traffic-share', data, {
            labelInterpolationFnc: function(value) {
              return Math.round(value / data.series.reduce(sum) * 100) + '%';
            },            
            low: 0,
            high: 8,
            donut: true,
            donutWidth: 20,
            donutSolid: true,
            fullWidth: false,
            showLabel: false,
            plugins: [
              Chartist.plugins.tooltip()
            ],
        });         
    }

    if (d.getElementById('loadOnClick')) {
        d.getElementById('loadOnClick').addEventListener('click', function () {
            var button = this;
            var loadContent = d.getElementById('extraContent');
            var allLoaded = d.getElementById('allLoadedText');
    
            button.classList.add('btn-loading');
            button.setAttribute('disabled', 'true');
    
            setTimeout(function () {
                loadContent.style.display = 'block';
                button.style.display = 'none';
                allLoaded.style.display = 'block';
            }, 1500);
        });
    }

    var scroll = new SmoothScroll('a[href*="#"]', {
        speed: 500,
        speedAsDuration: true
    });

    if(d.querySelector('.current-year')){
        d.querySelector('.current-year').textContent = new Date().getFullYear();
    }

    // Glide JS

    if (d.querySelector('.glide')) {
        new Glide('.glide', {
            type: 'carousel',
            startAt: 0,
            perView: 3
          }).mount();
    }


});
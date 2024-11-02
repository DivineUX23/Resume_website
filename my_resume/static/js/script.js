$('.navToggle').on('click', function (e) {
  e.preventDefault();
  $('body').toggleClass('navToggleActive');
});


$(window).scroll(function(){
  if ($(this).scrollTop() > 10) {
    $('body').addClass('fixedHeader');
  } else {
    $('body').removeClass('fixedHeader');
  }
});


var swiper = new Swiper(".testimonialSwiper", {
  navigation: {
    nextEl: ".test-swiper-button-next",
    prevEl: ".test-swiper-button-prev",
  },
});


var swiper = new Swiper(".certificatesSlider", {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".cert-swiper-button-next",
    prevEl: ".cert-swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    1024: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
  },
});


document.addEventListener("DOMContentLoaded", function () {
    
  if (document.getElementById('chat-page')) {

    let protocol = window.location.protocol === "https:" ? "wss://" : "ws://";
    let url = `${protocol}${window.location.host}/ws/data/`;
    const assistantSocket = new WebSocket(url);


    function scrollToBottom() {
      setTimeout(() => {
      window.scrollTo(0, document.body.scrollHeight);
  }, 0);
  }

    assistantSocket.onopen = function() {
        console.log("WebSocket connection established");
    };

    assistantSocket.onmessage = function(e) {
        let data = JSON.parse(e.data);
        console.log('Data:', data);

        if (data.type === 'chat_message') {
            console.log('Message:', data.message);
            let messages = document.getElementById('user_message');

            // Remove the loading indicator
            let loadingIndicator = document.getElementById('loading-indicator');
            if (loadingIndicator) {
                loadingIndicator.remove();
            }

            var converter = new showdown.Converter();

            let messageContent = converter.makeHtml(data.message);

            let messageDiv = document.createElement('li');
              messageDiv.classList.add('d-flex', 'justify-content-start', 'mb-4', 'fade-in-up');
              messageDiv.style.width = '95%';

              let span = document.createElement('span');
              messageDiv.appendChild(span);

              messages.appendChild(messageDiv);

              let typewriter = new Typewriter(span, {
                  loop: false,
                  delay: 3
              });

              typewriter.typeString(messageContent).start().callFunction(() => {
                  scrollToBottom();
              });
          }
    };

    
    assistantSocket.onclose = function(e) {
      alert("Connection lost. Please refresh this page to reconnect.");
    };


    let form = document.getElementById('chat_message_form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        let message = e.target.body.value;

        // Convert Markdown to HTML
        let messageContent = message;
        let messages = document.getElementById('user_message');

        let messageHTML = `
        <li class="d-flex justify-content-end mb-4 fade-in-up">
            <div class="bg-white shadow p-3" style="max-width: 95%; border-radius: 50px 50px 50px 50px;">
                <span>${messageContent}</span>
            </div>
        </li>`;

        messages.insertAdjacentHTML('beforeend', messageHTML);
        scrollToBottom();

        // Send the raw message text to the WebSocket
        assistantSocket.send(JSON.stringify({
            'message': message
        }));

        form.reset();

        // Add the loading indicator
        let loadingHTML = `
          <li id="loading-indicator" class="d-flex justify-content-start mb-4">
              <div class="bg-white p-3 rounded-end rounded-start-0" style="max-width: 75%;">
                  <div class="spinner-grow" role="status">
                    <span class="visually-hidden"></span>
                  </div>
              </div>
          </li>`;
        messages.insertAdjacentHTML('beforeend', loadingHTML);
        scrollToBottom();
    })
  }

});

document.addEventListener("DOMContentLoaded", function () {
  // Start the typing effect
  startTypingEffect();

});


function startTypingEffect() {
  
  //const texts = ["I think you know me", "I'm a {{ me.userprofile.title }}", "I'm {{ me.first_name|title }}."];
  const texts = ["Need a solid backend or API?", "I build solutions that scale", "I'm {{ me.first_name|title }} - Your backend guy."];

  const typingElement = document.querySelector('.typing');

  const typewriter = new Typewriter(typingElement, {
    loop: true,
    delay: 80,
  });

  texts.forEach(text => {
    typewriter.typeString(text)
      .pauseFor(2000) // Wait 2 seconds before typing the next string
      .deleteAll()
      .start();
  });
}


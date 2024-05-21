/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')


      /*Mostrar Menu*/
if(navToggle){
    navToggle.addEventListener('click', () =>{
        navMenu.classList.add('show-menu')
    })
}

/*Esconder Menu*/
if(navClose){
    navClose.addEventListener('click', () =>{
        navMenu.classList.remove('show-menu')
    })
}
/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll('.nav__link')

const linkAction = () =>{
    const navMenu = document.getElementById('nav-menu')
      //quando clicar em um nav__link remover a classe show-menu
      navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*=============== MUDAR MENU HEADER ===============*/
const blurHeader = () =>{
      const header = document.getElementById('header')
      //adicione uma classe se o deslocamento inferior for maior que 50 da janela de visualização
      this.scrollY >= 50 ? header.classList.add('blur-header')
                         :header.classList.remove('blur-header')
}
window.addEventListener('scroll', blurHeader)
/*=============== ADD BLUR HEADER ===============*/


/*=============== EMAIL JS ===============*/
const contactForm = document.getElementById('contact-form'),
      contactMessage = document.getElementById('contact-message')

const sendEmail = (e) =>{
    e.preventDefault()

    //serviceID -templateID - #form - publickey
    emailjs.sendForm('service_mvm7s2w','template_8clnsag','#contact-form','k1PR437LYgJYMf_p9')
      .then(() =>{
        //mostrar mensagem enviada
        contactMessage.textContent = 'Mensagem enviada com sucesso 🥳'

        //remove a mensagem após 5 segundos
        setTimeout(() =>{
            contactMessage.textContent = ''
        }, 5000)

        //Limpar campos
        contactForm.reset()
        }, () =>{
            //Mensagem de erro
            contactMessage.textContent = '🚨Falha ao enviar mensagem, tente novamente mais tarde.🚨'
        })
} 

contactForm.addEventListener('submit', sendEmail)

/*=============== SHOW SCROLL UP ===============*/ 
const scrollUp = () =>{
    const scrollUp = document.getElementById('scroll-up')
    //quando o scroll é maior que 350 da viewport adiciona a classe para mostrar o scroll-up
    this.scrollY >= 350 ? scrollUp.classList.add('show-scroll')
                        : scrollUp.classList.remove('show-scroll')
}
window.addEventListener('scroll', scrollUp)

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll('section[id]')

const scrollActive = () =>{
    const scrollDown = window.scrollY

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight,
        sectionTop = current.offsetTop -58,
        sectionId = current.getAttribute('id'),
        sectionClass = document.querySelector('.nav__menu a[href*=' + sectionId + ']')

        if(scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight){
            sectionClass.classList.add('active-link')
        }else{
            sectionClass.classList.remove('active-link')
        }
})
}
window.addEventListener('scroll', scrollActive)

/*=============== SCROLL REVEAL ANIMATION ===============*/

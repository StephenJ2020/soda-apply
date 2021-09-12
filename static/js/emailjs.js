if(window.location.pathname == '/contact') {
    document.getElementById('contact-form').addEventListener('submit', function(event) {
        event.preventDefault();
    
        const serviceID = 'service_sb29jwq';
        const templateID = 'contact_form';
    
        emailjs.sendForm(serviceID, templateID, this)
            .then(function() {
                console.log('SUCCESS!');
                document.getElementById("contact-form").reset();
            }, function(error) {
                console.log('FAILED...', error);
                document.getElementById("contact-form").reset();
            });
    });
}

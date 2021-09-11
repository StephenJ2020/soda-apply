function sendMail(contactForm) {
    emailjs.send("gmail", "contact_form", {
        "from_name": contactForm.fname.value,
        "from_email": contactForm.email.value,
        "contact_us": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
    return false;  // To block from loading a new page
}
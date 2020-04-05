function sendMail(contactMe) {
    emailjs.init("user_2XLNWuqeljGFG1tggK7In");
    emailjs.send("gmail", "nim-reads", {
        "from_name": contactMe.name.value,
        "from_email": contactMe.email.value,
        "message": contactMe.message.value
    })
        .then(
            resetForm(),
        );
    return false;

}

function resetForm() {
    let form = document.getElementById('myForm');
    form.reset();
}
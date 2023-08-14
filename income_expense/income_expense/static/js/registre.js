const usernameField=document.querySelector('#usernameField')
const usernamefedbackArea=document.querySelector('.invalid_feedback')
const emailField=document.querySelector('#emailField')
const emailFeedBackArea=document.querySelector('.emailFeedBackArea')

console.log('111111111111111111111111111111111');
emailField.addEventListener('keyup',(e)=>{
    const emailVal=e.target.value
    if(emailVal!=''){
        console.log('xxxxxxxx');
        fetch('/authentication/valide-email',{
            body:JSON.stringify({email:emailVal}),
            method:'POST',
        
        }).then(res=>{
            res.json().then(data=>{
                console.log(data);
                if(data.email_error){
                    emailField.classList.add('is-invalid')
                    emailFeedBackArea.style.display='block'
                    emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`
                }else{
                    emailFeedBackArea.style.display='none'
                    emailField.classList.remove('is-invalid')
                }
            })
        })
    }
})

usernameField.addEventListener('keyup',(e)=>{
    const usernameValue=e.target.value
    if(usernameValue!=''){
        fetch('/authentication/valide-username',{
            body:JSON.stringify({username:usernameValue}),
            method:'POST',
        
        }).then(res=>{
            res.json().then(data=>{
                if(data.username_error){
                    usernameField.classList.add('is-invalid')
                    usernamefedbackArea.style.display='block'
                    usernamefedbackArea.innerHTML=`<p>${data.username_error}</p>`
                }else{
                    usernamefedbackArea.style.display='none'
                    usernameField.classList.remove('is-invalid')
                }
            })
        })
    }


})
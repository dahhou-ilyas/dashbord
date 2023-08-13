const usernameField=document.querySelector('#usernameField')
const fedbackArea=document.querySelector('.invalid_feedback')

usernameField.addEventListener('keyup',(e)=>{
    const usernameValue=e.target.value

    if(usernameValue!=''){
        fetch('/authentication/valide-username',{
            body:JSON.stringify({username:usernameValue}),
            method:'POST',
        
        }).then(res=>{
            res.json().then(data=>{
                console.log(data);
                if(data.username_error){
                    usernameField.classList.add('is-invalid')
                    fedbackArea.style.display='block'
                    fedbackArea.innerHTML=`<p>${data.username_error}</p>`
                }else{
                    fedbackArea.style.display='none'
                    usernameField.classList.remove('is-invalid')
                }
            })
        })
    }


})
const searchField=document.querySelector('#searchField')

searchField.addEventListener('keyup',(e)=>{
    const searchValur=e.target.value;

    if(searchValur.trim().length>0){
        fetch('/search',{
            body:JSON.stringify({searchText:searchValur}),
            method:'POST',
        
        }).then(res=>{
            res.json().then(data=>{
                console.log(data);
            })
        })
    }
})
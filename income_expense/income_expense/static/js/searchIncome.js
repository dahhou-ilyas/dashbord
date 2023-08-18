

const searchField=document.querySelector('#searchField')
const table_output=document.querySelector('.table-output')
const app_table=document.querySelector('.app-table')
const pagination_container=document.querySelector('.pagination-container')
const table_body=document.querySelector('.table-body')

table_output.style.display="none";

searchField.addEventListener('keyup',(e)=>{
    const searchValur=e.target.value;

    if(searchValur.trim().length>0){
        pagination_container.style.display="none";
        table_body.innerHTML=""

        fetch('/income/search-income',{
            body:JSON.stringify({searchText:searchValur}),
            method:'POST',
        
        }).then(res=>{
            res.json().then(data=>{
                
                app_table.style.display="none";
                table_output.style.display="block";
                if(data.length===0){
                    table_output.innerHTML="no result found"
                }else{
                    data.forEach(item=>{
                        table_body.innerHTML+=`
                        <tr>
                            <td>${item.amount}</td>
                            <td>${item.source}</td>
                            <td>${item.description}</td>
                            <td>${item.date}</td>
                        </tr>
                        `
                    })
                }
            })
        })
    }else{
        table_output.style.display="none"
        pagination_container.style.display="block";
        app_table.style.display="block";
    }
})
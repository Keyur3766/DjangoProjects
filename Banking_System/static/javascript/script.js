document.getElementById("choice1").addEventListener('click',()=>{
    document.getElementById("usingACCOUNT").style.display="none"; 
    document.getElementById("usingUPI").style.display="block"; 
    document.getElementById("choice2").classList.remove('active')
    document.getElementById("choice1").classList.add('active')
})

document.getElementById("choice2").addEventListener('click',()=>{
    document.getElementById("usingACCOUNT").style.display="block"; 
    document.getElementById("usingUPI").style.display="none"; 
    document.getElementById("choice1").classList.remove('active')
    document.getElementById("choice2").classList.add('active')
})





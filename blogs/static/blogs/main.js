
document.addEventListener("DOMContentLoaded", ()=>{

	const myTextArea = document.querySelectorAll('[name="content"]');

	
	if(myTextArea.length!=0){

		const myCodeMirror = CodeMirror.fromTextArea(myTextArea[0],{
			lineNumbers: true
		});

		const txtArea = document.querySelectorAll('textarea');
		txtArea[1].addEventListener('change',()=>{
			txtArea[0].value = txtArea[1].value;
			console.log(txtArea[0].value)
		})
		console.log(txtArea)
	}
	

	const code_content = document.querySelector('.code-content');
	if(code_content!=null){
		const myCodeMirrorDetail = CodeMirror.fromTextArea(code_content,{
			lineNumbers: true
		});
	}
	

	// const detailArea = document.querySelectorAll('textarea');
	// txtArea[1].addEventListener('change',()=>{
	// 	txtArea[0].value = txtArea[1].value
	// })


});

// if (textarea!==null) {
// 	const myCodeMirror = 
// }


// class="textarea form-control"
// name="content"1px solid #ced4da
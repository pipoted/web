let relog = function () {
	console.log.apply(console, arguments)
}

let e = function (sel) {
	return document.querySelector(sel)
}

let todoTemplate = function(todo) {
	return `
	<divk class='todo-cell'>
		<button class='button-delete'>删除</button>
		<span>${todo}</span>
	</div>
	`
}
let b = e('#id-button-add')

b.addEventListener('click', function () {
	relog('click')
	let input = e('#id-input-todo')
	let todo = input.value
	relog('todo', todo)
	let todoCell = todoTemplate(todo)
	let todoList = e('.todo-list')
	todoList.insertAdjacentHTML('beforeend', todoCell)
})

let todoList = e('.todo-list')
todoList.addEventListener('click', function (event) {
	relog('click todolist', event)
	let self = event.target
	relog('被点击的元素是:', self)
	relog(self.classList)
	
	if (self.classList.contains('button-delete')) {
		relog('点到了删除按钮')
		self.parentElement.remove()
	} else {
		relog('点到的不是删除按钮')
	}
})




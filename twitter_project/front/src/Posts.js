import React, {Component} from "react";
import PostService from "./PostService";

const postService = new PostService();

export default class Posts extends Component {

    // прописываем основной конструктор
    constructor(props) {
        super(props)
        this.state = {
            data : [], // сюда загружаем посты, поэтому изначально тут пуста
            inputValue: ''  // сюда будем воодить новые посты
        }
        this.handleChange = this.handleChange.bind(this); // событие, когда изменили поле ввода
        this.handleSubmit = this.handleSubmit.bind(this); // событие, когда мы нажимаем на кнопку отправить пост
    }

    handleChange(event) {
    	this.setState({inputValue: event.target.value});
	}

	handleSubmit(event) {
    	postService.createPost({'text' : this.state.inputValue});
    	this.getData()
    	this.setState({inputValue : ''})
	}

    // прописываем то, как мы будем получать данные с сервера и сразу функцию загрузки данных
    // загружаем базу
    getData(){
        postService.getPost().then(result => {
            this.setState({data: result.data})
        })
    }

    // после загрузки, выполняем её
    componentDidMount(){
        this.getData()
    }

    // делаем функцию для лайков
    setLike(post) {
        postService.setLikePost(post.id)
        post.likeCount += 1
        this.forceUpdate()
    }

    // Циклично загружаем все посты, попутно добавляя функции по нажатию кнопок Like, 
    // передавая в качестве аргумента итерируемый объект post. Еще сразу добавляем прописанные события по вводу нового поста
    render(){
        return(
            <div id='posts'>
                {this.state.data.map(post=>
                    <div id = {'post_' + post.id}>
                        <p>{post.text}</p>
                        <button onClick={() => this.setLike(post)}> {post.likesCount} </button>
                        <p>Date : {post.date}</p>
                        <hr/>
                    </div>
                )}
                <input type='text' onChange={this.handleChange} value={this.state.inputValue}></input>
                <button onClick = {this.handleSubmit}>Send</button>
            </div>
        )
    }
}
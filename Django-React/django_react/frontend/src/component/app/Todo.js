import React, { Component } from 'react';
import {Form} from 'react-bootstrap'
import axios from 'axios';
import './Todo.css';


class Todo extends Component {
    constructor(props){
        super(props);
        this.state = {
            posts: [],
            addname : '',
            rmvnum : 0
        };
        this.addlist = this.addlist.bind(this);
        this.rmvlist = this.rmvlist.bind(this);
        this.displaylist = this.displaylist.bind(this);
    }

    displaylist = () => {
        const list = this.state.posts;
        return (
        <ul className='todoul'>
            {list.map(item => (
                <Form key={item.id} method="POST" onSubmit={this.rmvlist} >
                    <li  className='todoli shadow' >
                            { item.title }
                            <button
                                type="submit"
                                className="removeBtn"
                                name='rmvnum'
                                id={item.id}
                                onClick={this.onclick}
                                >
                                <i aria-hidden='true' className='fa fa-trash-o'>X</i>
                            </button>
                    </li>
                </Form>
            ))}
        </ul>
        );
    }


    // 여기가 django 서버에서 url로 데이터 받아오는 부분
    getpost = async() => {
        const {data} = await axios.get('http://localhost:8000/Todo/');
        this.setState({posts:{data}.data});
    }
    async componentDidMount(){
        this.getpost();
    }

    addlist = async(e) =>{
        e.preventDefault();
        const {data} = await axios.post('/Todo/create/', {'addname':this.state.addname});
        this.setState({posts:{data}.data});
        this.displaylist();

    }
    rmvlist = async(e) =>{
        e.preventDefault();
        const {data} = await axios.post('/Todo/delete/', {'rmvnum':this.state.rmvnum});
        this.setState({posts:{data}.data});
        this.displaylist();
    }

    onchange = (e)=>{
        this.setState({[e.target.name]:e.target.value});
    }

    onclick = (e) => {
        this.setState({[e.target.name]:e.target.id});
    }

    // react로 페이지 만드는 부분
    render() {
        return (
        <div className='container'>
            <div className='todoheader'>
                <h1>To Do List</h1>
            </div>
            <div className='inputBox shadow todoheader'>
                <Form method='POST' onSubmit={this.addlist}>
                    <Form.Group className='d-flex'>
                        <Form.Control
                            type='text'
                            name='addname'
                            placeholder="할일 적기!"
                            onChange={this.onchange}
                        />
                        <button type="submit" className='addContainer '>
                            <i aria-hidden='true' className='addBtn fa fa-plus mb-2'>+
                            </i>
                        </button>

                    </Form.Group>
                </Form>
            </div>
            <hr/>
            <div className='todobody'>
                {this.displaylist()}
            </div>
        </div>
        );
    }
}
export default Todo;

import React, { Component } from 'react';
import {Button,Form, FormGroup, Input, Row, Col} from 'reactstrap'
import axios from 'axios';

class Todo extends Component {
    constructor(props){
        super(props);
        this.state = {
            posts: []
        };
        this.addlist = this.addlist.bind(this);
    }


    // 여기가 django 서버에서 url로 데이터 받아오는 부분
    getpost = async() => {
        const {data}= await axios.get('http://localhost:8000/Todo/');
        this.setState({posts:{data}.data});
        console.log({data});
    }
    async componentDidMount(){
        this.getpost();
    }

    addlist = async() =>{
        console.log();
        const {asdf} = await axios.post('http://localhost:8000/Todo/create/');
    }

    // react로 페이지 만드는 부분
    render() {
        return (
        <div className='container'>
            <div className='todoheader'>
                <h1>To Do List <small> made by JISU </small></h1>
            </div>

            <Form method='POST' action='Todo/create/'>
                <Row form>
                    <Col md={11}>
                        <FormGroup className='mb-2 mr-sm-2 mb-sm-0'>
                            <Input type='text' id='todoContent' name='todoContent' placeholder="할일 적기!"/>
                        </FormGroup>
                    </Col>
                    <Col md={1}>
                        <FormGroup className='mb-2 mr-sm-2 mb-sm-0'>
                            <span className="input-group-btn">
                                    <Button type="submit" >추가</Button>
                            </span>
                        </FormGroup>
                    </Col>
                </Row>
            </Form>
            <hr/>
            <div className='todobody'>
            {this.state.posts.map(item => (
                <div key={item.id} >
                    <Form method="POST" action="Todo/delete/" >
                        <div className="input-group" name='todo1'>
                            <li className="list-group-item">{ item.title }</li>
                            <input type="hidden" id="todoNum" name="todoNum" value={ item.id }></input>
                            <span className="input-group-addon">
                                <Button type="submit" className="btn btn-danger">완료</Button>
                         </span>
                        </div>
                    </Form>
                </div>
            ))}
            </div>
        </div>
        );
    }
}
export default Todo;

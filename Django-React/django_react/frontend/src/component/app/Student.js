import React,{Component} from 'react';
import axios from 'axios';
import './Student.css';
import {Modal, Form, Table} from 'react-bootstrap';

class Student extends Component{
    constructor(props){
        super(props);
        this.state = {
            students : [],
            infomodal : false,
            addmodal : false,
            number : 0,
            name : '',
            age : 0,
            major : ''
        }
    }
    getstd = async() =>{
        await axios.get('Student')
            .then(res=>{this.setState({students: res.data}); });
    }
    componentDidMount(){
        this.getstd();
    }
    studentadd = () =>{
        this.setState({addmodal: !this.state.addmodal});
    }
    studentinfo = (e) =>{
        const infos = e;
        console.log(infos);
        this.setState({infomodal: !this.state.infomodal});
    }
    addstd = async() =>{
        const {number, name, age, major} = this.state;
        await axios.post('Student/', {number, name, age, major})
            .then(res=>{
                console.log(res);
                if (res.status === 201){
                    this.setState({addmodal:!this.state.addmodal});
                    this.getstd();
                }
                else{
                    alert('다시 입력해주세요!');
                }
            })
    }
    deletestd = async(e) =>{
        const pk = e.target.id;
        await axios.delete('Student/'+pk)
            .then(res=>{
                if(res.status === 204){
                    alert('삭제되었습니다.');
                    this.getstd();
                }
            })
    }
    updatestd = async(e) =>{
        const {number, name, age, major} = this.state;
        await axios.put('Student/', {number, name, age, major})
            .then(res=>{
                this.setState({addmodal:!this.state.addmodal});
                this.getstd();
            })
    }
    onChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    }

    render(){

        return(
            <div className='container '>
                <div className='text-center'>
                    <h2> 수강생 정보 조회 </h2>
                </div>
                <Table  bordered hover className= 'text-center'>
                    <thead><tr>
                        <th>학번</th>
                        <th>이름</th>
                        <th>나이</th>
                        <th>전공</th>
                        <th colSpan='2'>
                            <button className='btn-add'onClick={()=>this.studentadd()}>수강생 추가</button>
                        </th>
                        <Modal show={this.state.addmodal} onHide={()=>this.studentadd()}>
                            <Modal.Header closeButton>
                                <Modal.Title>수강생 추가</Modal.Title>
                            </Modal.Header>
                            <Modal.Body>
                                <Form.Group>
                                    <Form.Label>학번: </Form.Label>
                                    <Form.Control type='number' name='number' onChange={this.onChange} />
                                    <Form.Label>이름: </Form.Label>
                                    <Form.Control type='text' name='name' onChange={this.onChange}/>
                                    <Form.Label>나이: </Form.Label>
                                    <Form.Control type='number' name='age' onChange={this.onChange}/>
                                    <Form.Label>전공: </Form.Label>
                                    <Form.Control type='text' name='major' onChange={this.onChange}/>
                                </Form.Group>
                            </Modal.Body>
                            <Modal.Footer>
                                <button onClick={()=>this.studentadd()}>취소</button>
                                <button onClick={()=>this.addstd()}>제출</button>
                            </Modal.Footer>
                        </Modal>
                    </tr></thead>
                    <tbody>
                        {this.state.students.map(std=>(
                            <tr key={std.id} >
                                <td>{std.number}</td>
                                <td>{std.name}</td>
                                <td>{std.age}</td>
                                <td>{std.major}</td>
                                <td><button className='btn-udt'onClick={(e)=>this.studentinfo(e)}>수정</button></td>
                                <td><button className='btn-dlt'id={std.id} onClick={(e)=>this.deletestd(e)}>삭제</button></td>
                            </tr>
                         ))}
                         <Modal show={this.state.infomodal} onHide={()=>this.studentinfo()}>
                            <Modal.Header closeButton>
                                <Modal.Title>수강생 정보 수정</Modal.Title>
                            </Modal.Header>
                            <Modal.Body>
                                <Form.Group>
                                    <Form.Label>학번: </Form.Label>
                                    <Form.Control type='number' name='number' onChange={this.onChange}/>
                                    <Form.Label>이름: </Form.Label>
                                    <Form.Control type='text' name='name' onChange={this.onChange}/>
                                    <Form.Label>나이: </Form.Label>
                                    <Form.Control type='number' name='age' onChange={this.onChange}/>
                                    <Form.Label>전공: </Form.Label>
                                    <Form.Control type='text' name='major' onChange={this.onChange}/>
                                </Form.Group>
                            </Modal.Body>
                            <Modal.Footer>
                                <button onClick={()=>this.studentinfo()}>취소</button>
                                <button onClick={()=>this.updatestd()}>수정</button>
                            </Modal.Footer>
                        </Modal>
                    </tbody>
                </Table>
            </div>
        );
    }
}


export default Student;
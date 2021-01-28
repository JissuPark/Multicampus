import React, { Component } from 'react';

class Home extends Component {
    state = {
        posts: []
    };


    render() {
        return (
        <pre className='blockquote'>
            {`안녕하세요.\n저는 백엔드 개발을 공부하고 있는 박지수라고 합니다.`}
        </pre>
        );
    }
}
export default Home;

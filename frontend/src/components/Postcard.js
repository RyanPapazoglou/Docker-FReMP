import React from 'react';
import { Button, Card, Icon, Label } from 'semantic-ui-react';
import moment from "moment";
import { Link } from "react-router-dom";

const Postcard = ({post: { body, createdAt, id, username, likeCount, commentCount, likes }}) => {
    const likePost = () => {
        console.log("Liked");
    }

    const commentOnPost = () => {
        console.log("comment");
    }

    return (
        <Card fluid>
            <Card.Content>
                <Card.Header>{username}</Card.Header>
                <Card.Meta as={Link} to={`/posts/${id}`}>{moment(createdAt).fromNow(true)}</Card.Meta>
                <Card.Description>
                    {body}
                </Card.Description>
            </Card.Content>
            <Card.Content extra>
                <Button as='div' labelPosition='right'>
                    <Button color='teal' basic onClick={likePost}>
                        <Icon name='heart' />
                        Like
                    </Button>
                    <Label as='a' basic color='teal' pointing='left'>
                        {likeCount}
                    </Label>
                </Button>
                <Button as='div' labelPosition='right'>
                    <Button color='blue' basic onClick={commentOnPost}>
                        <Icon name='comments' />
                    </Button>
                    <Label as='a' basic color='blue' pointing='left'>
                        {commentCount}
                    </Label>
                </Button>
            </Card.Content>
        </Card>
    )
}

export default Postcard;
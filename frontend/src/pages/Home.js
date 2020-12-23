import React from 'react';
import { Grid, Transition} from 'semantic-ui-react';
import Postcard from "../components/Postcard";


function Home() {
    const { data, loading, error } = {}

    return (
        <Grid columns={3} divided>
            <Grid.Row className="page-title">
                <h1>Recent Posts</h1>
            </Grid.Row>
            <Grid.Row>
                {loading ?
                    (
                        <h1>Loading posts..</h1>
                    ) : (
                        data && <Transition.Group>
                            {data.getPosts &&
                            data.getPosts.map((post) => (
                                <Grid.Column key={post.id} style={{ marginBottom: 20 }}>
                                    <Postcard post={post} />
                                </Grid.Column>
                            ))}
                        </Transition.Group>
                    )
                }
            </Grid.Row>
        </Grid>
    )
}

export default Home;
import React, { useContext } from 'react';
import { Route, Redirect } from 'react-router-dom';

import { AuthContext } from "../context/auth";

function AuthRoute ({ component: Component, ...props }) {
    const { user } = useContext(AuthContext);

    return (
        <Route {...props} render={props => user ? <Redirect to={"/"} /> : <Component {...props}/> } />
    )
}

export default AuthRoute;
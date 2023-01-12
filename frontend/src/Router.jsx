import { Route, Routes } from 'react-router-dom';
import Home from './containers/Landing';
import MyProfile from "./containers/MyProfile";

const Router = () => {
    return (
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/" element={<MyProfile />} />
        </Routes>
    );
};
export default Router;

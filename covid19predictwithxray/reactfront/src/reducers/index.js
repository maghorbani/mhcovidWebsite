import { combineReducers } from "redux";
// import users from "./users";
// import errors from "./errors";
import imageReducer from "./images";
import uiReducer from "./ui";

export default combineReducers({
  images: imageReducer,
  ui: uiReducer,
  // users,
  // errors,
});

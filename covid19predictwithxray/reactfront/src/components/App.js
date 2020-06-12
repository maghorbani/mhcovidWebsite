import React, { Component, Fragment } from "react";
import PredictionForm from "./PredictionForm";
import clsx from "clsx";
import Header from "../layouts/Header";
import Footer from "../layouts/Footer";
import { connect } from "react-redux";
import { compose } from "redux";
import { withStyles } from "@material-ui/core/styles";
import PropTypes from "prop-types";

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import AboutUs from "./pages/AboutUs";
import Error404 from "./pages/Error404";
import GitRepos from "./pages/GitRepos";
import Acknowledgement from "./pages/Acknowledgement";

const styles = (theme) => ({
  root: {
    height: "100%",
  },
  content: {
    // zIndex: theme.zIndex.drawer + 1,
    height: "100%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",

    marginLeft: 73,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  contentShift: {
    marginLeft: 240,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
});

class App extends Component {
  static propTypes = {
    classes: PropTypes.object.isRequired,
    drawerOpen: PropTypes.bool.isRequired,
  };
  render() {
    const { classes, theme, drawerOpen } = this.props;
    return (
      <Router>
        <div className={classes.root}>
          <Header />
          <div
            className={clsx(classes.content, {
              [classes.contentShift]: drawerOpen,
            })}
          >
            <Switch>
              <Route exact path="/">
                <PredictionForm />
              </Route>
              <Route path="/AboutUs">
                <AboutUs />
              </Route>
              <Route path="/Repos">
                <GitRepos />
              </Route>
              <Route path="/acknowledgement">
                <Acknowledgement />
              </Route>
              <Route>
                <Error404 />
              </Route>
            </Switch>
            <Footer />
          </div>
        </div>
      </Router>
    );
  }
}

const mapStateToProps = (state) => ({
  drawerOpen: state.ui.drawerOpen,
});

export default compose(
  withStyles(styles, { withTheme: true }),
  connect(mapStateToProps, {})
)(App);

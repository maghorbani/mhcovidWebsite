import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { compose } from "redux";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Typography from "@material-ui/core/Typography";

const styles = (theme) => ({
  root: {
    marginLeft: "20px",
    display: "flex",
    height: "100%",
    paddingTop: "100px",
    alignItems: "flex-start",
  },
});

export class GitRepos extends Component {
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <div className={classes.demo}>
          <Typography variant="h4">GitRepos</Typography>
          <List>
            <ListItem>
              <ListItemText
                primary="MHCovid python module, Developed by Mohammad Hossein Amini"
                secondary={
                  <a
                    href="https://github.com/M-H-Amini/MHCovid"
                    target="_blank"
                  >
                    GitHub Link
                  </a>
                }
              />
            </ListItem>
            <ListItem>
              <ListItemText
                primary="WebApplication server and front side source, Developed by Mohammad Ali Ghorbani"
                secondary={
                  <a
                    href="https://github.com/maghorbani/mhcovidWebsite"
                    target="_blank"
                  >
                    GitHub Link
                  </a>
                }
              />
            </ListItem>
          </List>
        </div>

        {/* Special thanks to... 1- Dr.Menhaj, Dr.Talebi and Dr.Sharifi for their
        supports... 2- Dr.Mirahmadi, Dr.Javadi, Dr.Babakhani for their medical
        advices... 3- Dr.Ashnaee, Mr.Alipur for their supports... 4- Those who
        gather datasets of COVID-19 chest X-ray on github and kaggle
        https://github.com/ieee8023/covid-chestxray-dataset
        https://www.kaggle.com/praveengovi/coronahack-chest-xraydataset */}
      </div>
    );
  }
}

export default compose(withStyles(styles, {}))(GitRepos);

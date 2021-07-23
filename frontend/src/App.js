import React, { useState } from "react";
import { Tabs } from "antd";

import { UserData } from "./components/UserData/UserData";
import { MeetingAttendee } from "./components/MeetingAttendee/MeetingAttendee";
import { Gallery } from "./components/Gallery/Gallery";
import { isMobileCheck } from "./helpers/checkMobileTablet";
import { Login } from "./components/Login/Login";

import "./App.css";

const { TabPane } = Tabs;

const App = () => {
  const [hasAccess, setHasAccess] = useState(true);
  const isMobile = isMobileCheck();

  return (
    <div className="App">
      <header className="App-header">
        {hasAccess ? (
          <div className="App-Container">
            <Tabs defaultActiveKey="1" centered={isMobile}>
              <TabPane tab={isMobile ? "User in Database" : "User in Database"} key="1">
                <UserData />
              </TabPane>
              <TabPane tab={isMobile ? "Meetup" : "Meetup attendees"} key="2">
                <MeetingAttendee />
              </TabPane>
              <TabPane tab={isMobile ? "Images" : "User Images"} key="3">
                <Gallery />
              </TabPane>
            </Tabs>
          </div>
        ) : (
          <Login setHasAccess={setHasAccess} />
        )}
      </header>
    </div>
  );
};

export default App;

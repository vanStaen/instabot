import React, { useState } from "react";
import { Tabs } from "antd";

import { AccountData } from "./components/AccountData/AccountData";
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
                <AccountData />
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

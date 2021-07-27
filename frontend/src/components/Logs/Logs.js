import React, { useState, useEffect } from "react";
import { getLogs } from "../../calls/getLogs";7
import { isMobileCheck } from "../../helpers/checkMobileTablet";
import { Table } from "antd";

import "./Logs.css";

export const Logs = () => {
  const [logsData, setLogsData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const isMobile = isMobileCheck();

  const fetchLogs = async () => {
    try {
      const fetchedData = await getLogs();
      setLogsData(fetchedData);
    } catch (err) {
      console.log(err);
    }
    setIsLoading(false);
  };

  const columns = [
    {
      title: "Timestamp",
      dataIndex: "time",
      key: "time",
      sorter: (a, b) => a.id - b.id,
      responsive: ["lg"],
    },
    {
      title: "Level",
      dataIndex: "level",
      key: "level",
      defaultSortOrder: "ascend",
      sorter: (a, b) => {
        if (!a.level) {
          return +1;
        }
        if (!b.level) {
          return -1;
        }
        return a.level.localeCompare(b.level);
      },
    },
    {
      title: "Message",
      dataIndex: "message",
      key: "message",
    },
  ];

  useEffect(() => {
    fetchLogs();
  }, []);

  return isLoading ? (
    <div>Loading</div>
  ) : (
      <div className="ListData">
        <Table
          dataSource={logsData}
          columns={columns}
          pagination={{
            position: ["bottomCenter"],
            defaultPageSize: "20",
            hideOnSinglePage: true,
          }}
          size={isMobile ? "small" : "large"}
        />
      </div>
    );
};

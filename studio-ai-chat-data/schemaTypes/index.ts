export const schemaTypes = [{
    name: "chat",
    title: "Chat Messages",
    type: "document",
    fields: [
      {
        name: "question",
        title: "User Question",
        type: "string",
      },
      {
        name: "answer",
        title: "AI Response",
        type: "text",
      },
      {
        name: "timestamp",
        title: "Timestamp",
        type: "datetime",
        options: {
          dateFormat: "YYYY-MM-DD",
          timeFormat: "HH:mm:ss",
          calendarTodayLabel: "Today",
        },
      },
    ],
  }]

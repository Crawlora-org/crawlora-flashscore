import { FlashscoreClient } from "../src/index.js";

const client = new FlashscoreClient({ apiKey: "test-key" });
void client.calendar({"category": "tennis-atp"});
void client.request("flashscore-calendar", {"category": "tennis-atp"});
const streamResponse: Promise<Response> = client.request("flashscore-calendar", {"category": "tennis-atp"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("flashscore-calendar", {"category": "tennis-atp"}, { responseType: "stream" });
const directStream: Promise<Response> = client.calendar({"category": "tennis-atp"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("flashscore-calendar", {"category": "tennis-atp"}, { responseType: "text" });
const rawText: Promise<string> = client.request("flashscore-calendar", {"category": "tennis-atp"}, { responseType: "text" });
void rawText;


void client.calendarCategories();
void client.request("flashscore-calendar-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.calendar();

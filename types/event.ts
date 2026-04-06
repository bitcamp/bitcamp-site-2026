export interface ParsedEvent {
  id: string;
  title: string;
  description: string;
  startTime: string;
  endTime: string;
  location: string;
  zoom_email: string;
  zoom_link: string;
  type: string;
  speakers?: string[];
  links?: {
    title: string;
    url: string;
  }[];
}

export interface CalculatedEvent {
  id: string;
  title: string;
  description: string;
  location: string;
  type: string;
  zoom_email: string;
  zoom_link: string;
  speakers?: string[];
  links?: {
    title: string;
    url: string;
  }[];
  startTimeMs: number;
  endTimeMs: number;
  startRow: number;
  rowSpan: number;
  colSpan?: number;
}

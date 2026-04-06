<script setup lang="ts">
import { VueFinalModal } from "vue-final-modal";
import dayjs from "dayjs";
import type { CalculatedEvent } from "../types/event";

defineProps<{
  modelValue: boolean;
  selectedEvent?: CalculatedEvent;
}>();

const emit = defineEmits<{
  (e: "update:modelValue", value: boolean): void;
  (e: "close"): void;
}>();

function formatCategory(category: string | undefined) {
  if (!category) return "";
  return category
    .split("-")
    .map((word) => word[0].toUpperCase() + word.slice(1))
    .join(" ");
}

function formatTime(startTimeMs?: number, endTimeMs?: number) {
  if (!startTimeMs || !endTimeMs) return "";
  return `${dayjs(startTimeMs).format("dddd")}, ${dayjs(startTimeMs).format(
    "h:mm A",
  )} - ${dayjs(endTimeMs).format("h:mm A")}`;
}

function normalizeUrl(url?: string) {
  if (!url) return "";
  if (/^https?:\/\//i.test(url)) return url;
  return `https://${url}`;
}

function closeModal() {
  emit("update:modelValue", false);
  emit("close");
}
</script>

<template>
  <VueFinalModal
    :modelValue="modelValue"
    @update:modelValue="$emit('update:modelValue', $event)"
    class="modal"
    :content-class="'modal-content ' + selectedEvent?.type"
    overlay-transition="vfm-fade"
    content-transition="vfm-fade"
  >
    <div class="modal-header">
      <h1 class="event-title">{{ selectedEvent?.title }}</h1>
      <button class="close-modal-button" @click="closeModal">×</button>
    </div>
    <div class="modal-body">
      <p class="event-category">{{ formatCategory(selectedEvent?.type) }}</p>
      <div class="event-details">
        <p class="event-time">
          {{ formatTime(selectedEvent?.startTimeMs, selectedEvent?.endTimeMs) }}
        </p>
        <p v-if="selectedEvent?.location" class="event-location">
          {{ selectedEvent.location }}
        </p>
      </div>
      <p class="event-description">{{ selectedEvent?.description }}</p>
      <div
        v-if="selectedEvent?.zoom_email || selectedEvent?.zoom_link"
        class="event-join-card"
      >
        <p class="event-join-label">Join event</p>
        <div class="event-join-actions">
          <a
            v-if="selectedEvent?.zoom_email"
            class="event-join-link"
            :href="`mailto:${selectedEvent.zoom_email}`"
          >
            {{ selectedEvent.zoom_email }}
          </a>
          <a
            v-if="selectedEvent?.zoom_link"
            class="event-join-link"
            :href="normalizeUrl(selectedEvent.zoom_link)"
            target="_blank"
            rel="noreferrer"
          >
            Open Zoom link
          </a>
        </div>
      </div>
    </div>
  </VueFinalModal>
</template>

<style lang="scss">
@import "../assets/css/schedule.scss";

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  display: flex;
  flex-direction: column;
  padding: 1.1rem;
  border-style: solid;
  border-radius: 0.75rem;
  border-width: 0.25rem;
  box-shadow: 0.4rem 0.4rem 1.2rem rgba(black, 0.5);
  width: 50rem;
  max-width: 90vw;
  margin: 0;
  position: relative;
  z-index: 1001;
  background-color: rgba(0, 0, 0, 0.8);
  overflow: hidden;

  &.main-event {
    background-color: $COLOR_MAIN_EVENT;
    border-color: $COLOR_MAIN_EVENT_BORDER;
  }
  &.workshop-event {
    background-color: $COLOR_WORKSHOP;
    border-color: $COLOR_WORKSHOP_BORDER;
  }
  &.mini-event {
    background-color: $COLOR_MINI_EVENT;
    border-color: $COLOR_MINI_EVENT_BORDER;
  }
  &.sponsor-event {
    background-color: $COLOR_SPONSOR;
    border-color: $COLOR_SPONSOR_BORDER;
  }
  &.food-event {
    background-color: $COLOR_FOOD;
    border-color: $COLOR_FOOD_BORDER;
  }
}
.modal-content > * + * {
  margin: 0.35rem 0;
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}
.close-modal-button {
  background: none;
  border: none;
  font-size: 2rem;
  color: white;
  cursor: pointer;
  padding: 0.5rem;
  line-height: 1;
  opacity: 0.8;
  transition: opacity 0.2s;

  &:hover {
    opacity: 1;
  }
}
.event-title {
  flex: 1;
  margin: 0;
}
.event-category {
  font-size: 1.9rem;
  color: rgba(white, 0.9);
  margin-top: -0.25rem;
  margin-bottom: 1rem;
}

.event-details {
  display: grid;
  gap: 0.6rem;
}

.event-time {
  font-size: 1.5rem;
  color: rgba(white, 0.75);
  margin-bottom: 0.25rem;
}
.event-location {
  font-size: 1.5rem;
  color: rgba(white, 0.75);
}

.event-join-card {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-top: 1rem;
  padding: 0;
  background: none;
  border: none;
  box-shadow: none;
}

.event-join-label {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(white, 0.7);
}

.event-join-actions {
  display: block;
}

.event-join-link {
  display: inline-block;
  margin-top: 0.2rem;
  padding: 0;
  background: none;
  border: none;
  color: white;
  font-size: 1.35rem;
  text-decoration: underline;
  word-break: break-all;
  opacity: 0.9;
  transition: opacity 0.2s ease;

  &:hover {
    opacity: 1;
  }
}

.event-description {
  margin-top: 1rem;
  font-size: 1.8rem;
  line-height: 1.45;
  white-space: pre-wrap;
}
</style>

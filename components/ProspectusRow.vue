<template>
  <div class="Rtable-cell Rtable-category-cell" :class="header">
    <a
      v-if="header !== 'first-row Rtable-category-cell-full'"
      class="tooltips direction"
      :description="description"
      :title="categoryName"
    >
      <img
        src="../assets/img/icons/question-mark-black.svg"
        alt="Question Mark"
      />
    </a>
    <div style="display: flex; flex-direction: column">
      <div v-if="!description">
        <span
          style="
            color: var(--color-dark-text);
            margin-left: 1rem;
            margin-top: 0.5rem;
          "
        >
          {{ categoryName }}
        </span>
      </div>
      <div v-else>
        <span style="color: var(--color-dark-text)">
          {{ categoryName }}
        </span>
      </div>
      <span
        v-if="subText"
        style="font-size: 1.25rem; color: var(--color-dark-text)"
        >{{ subText }}</span
      >
    </div>
  </div>

  <div
    v-for="(arg, index) in args"
    :key="index"
    class="Rtable-cell"
    :class="'Rtable-cell-' + tierNames[index]"
  >
    <p v-if="arg === 'check-b'">
      <img src="../assets/img/icons/check-black.svg" alt="Checkmark" />
    </p>
    <p v-else-if="arg === 'check-w'">
      <img src="../assets/img/icons/check-white.svg" alt="Checkmark" />
    </p>
    <p v-else>
      <span v-if="typeof arg === 'string' && arg.includes('check')">
        <span v-if="index < 2" style="color: var(--color-dark-text)">
          {{ stripCheckMarker(arg) }}
        </span>
        <span v-else>
          {{ stripCheckMarker(arg) }}
        </span>
        <br />
        <span
          style="display: flex; justify-content: center"
          v-if="arg.includes('check-b')"
        >
          (&nbsp;<img
            style="width: 1.75rem"
            src="../assets/img/icons/check-black.svg"
            alt="Checkmark"
          />&nbsp;)
        </span>
        <span
          style="display: flex; justify-content: center"
          v-if="arg.includes('check-w')"
        >
          (&nbsp;<img
            style="width: 1.75rem"
            src="../assets/img/icons/check-white.svg"
            alt="Checkmark"
          />&nbsp;)
        </span>
      </span>
      <span v-else-if="index < 2" style="color: var(--color-dark-text)">
        {{ arg }}
      </span>
      <span v-else>
        {{ arg }}
      </span>
    </p>
  </div>
</template>

<script>
export default {
  name: "ProspectusRow",
  props: {
    args: {
      type: Array,
      required: true,
    },
    tierNames: {
      type: Array,
      required: true,
    },
    categoryName: {
      type: String,
      required: true,
    },
    subText: {
      type: String,
      required: false,
    },
    header: {
      type: String,
      required: false,
    },
    description: {
      type: String,
      required: true,
    },
  },
  methods: {
    stripCheckMarker(arg) {
      return arg.replace("check-b", "").replace("check-w", "").trim();
    },
  },
};
</script>

<style scoped></style>

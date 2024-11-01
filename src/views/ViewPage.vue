<template>
  <div class="container">
    <!-- Left: Videos with labels -->
    <div class="left">
      <div v-for="(video, index) in mediaList" :key="index" class="video-container">
        <p>{{ video.text }}</p>
        <video autoplay loop muted>
          <source :src="video.videoSrc" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>

    <!-- Middle: Images with labels -->
    <div class="middle">
      <div v-for="(image, index) in mediaList" :key="index" class="image-container">
        <p>已截图：{{ image.text }}</p>
        <img :src="image.imageSrc" v-if="showImages[index]" alt="Displayed Image" />
      </div>
    </div>

    <!-- Right: Typing text with separated parts -->
    <div class="right">
      <!-- Title and Text for Left section -->
      <div>
        <h3 class="title breathing-flash">左侧</h3>
        <div v-if="showLeftParkingText">
          <div v-for="(text, index) in leftParkingText" :key="index" class="info-text">
            <span class="red-text">{{ text.type }} {{ text.number }}：</span>
            <span :class="text.status === '无车' ? 'green-text' : 'orange-text'">{{ text.status }}</span>
            <span class="red-text"> {{ text.type2 }} {{ text.number2 }}：</span>
            <span :class="text.status2 === '无车' ? 'green-text' : 'orange-text'">{{ text.status2 }}</span>
          </div>
        </div>
      </div>

      <!-- Title and Text for Right section -->
      <div>
        <h3 class="title breathing-flash">右侧</h3>
        <div v-if="showRightParkingText">
          <div v-for="(text, index) in rightParkingText" :key="index" class="info-text">
            <span class="red-text">{{ text.type }} {{ text.number }}：</span>
            <span :class="text.status === '无车' ? 'green-text' : 'orange-text'">{{ text.status }}</span>
            <span v-if="text.type2" class="red-text"> {{ text.type2 }} {{ text.number2 }}：</span>
            <span v-if="text.type2" :class="text.status2 === '无车' ? 'green-text' : 'orange-text'">{{ text.status2 }}</span>
          </div>
        </div>
      </div>

      <!-- Monitoring section -->
      <div>
        <h3 class="title breathing-flash">监控</h3>
        <p v-if="showCarPassCount" class="info-text">有车经过: {{ carPassCount }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mediaList: [
        { videoSrc: "/official_car_demo_1.mp4", imageSrc: "/static/car_demo_1.jpg", text: "监控摄像头：左" },
        { videoSrc: "/official_car_demo_2.mp4", imageSrc: "/static/car_demo_2.jpg", text: "监控摄像头：右" },
        { videoSrc: "/official_car_demo_3.mp4", imageSrc: "/static/car_demo_3.png", text: "入口摄像头" },
      ],
      showImages: [false, false, false], // Controls when each image is shown
      leftParkingText: [
        { type: "横向停车", number: 1, status: "占用", type2: "竖向停车", number2: 1, status2: "无车" },
        { type: "横向停车", number: 2, status: "占用", type2: "竖向停车", number2: 2, status2: "占用" },
        { type: "横向停车", number: 3, status: "无车", type2: "竖向停车", number2: 3, status2: "占用" },
      ],
      rightParkingText: [
        { type: "竖向停车", number: 1, status: "无车", type2: "竖向停车", number2: 2, status2: "占用" },
        { type: "竖向停车", number: 3, status: "无车", type2: "竖向停车", number2: 4, status2: "占用" },
        { type: "竖向停车", number: 5, status: "占用" }
      ],
      carPassCount: 1, // Number of cars passed in monitoring section
      showLeftParkingText: false,
      showRightParkingText: false,
      showCarPassCount: false,
    };
  },
  mounted() {
    this.startSequence();
    this.startDisplay(); // Start the sequential display of text
  },
  methods: {
    startSequence() {
      // Show images with delays
      setTimeout(() => {
        this.showImages[0] = true;
      }, 1000);

      setTimeout(() => {
        this.showImages[1] = true;
      }, 5000);

      setTimeout(() => {
        this.showImages[2] = true;
      }, 13000);
    },
    startDisplay() {
      // Display left parking text after 1 second
      setTimeout(() => {
        this.showLeftParkingText = true;
      }, 2000);

      // Display right parking text after 2 seconds
      setTimeout(() => {
        this.showRightParkingText = true;
      }, 6000);

      // Display car pass count after 3 seconds
      setTimeout(() => {
        this.showCarPassCount = true;
      }, 14000);
    },
  },
};
</script>

<style scoped>
/* Flex container for the three sections */
.container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  height: 100vh;
  padding: 10px;
  gap: 10px;
  overflow: hidden; /* Prevent scrolling */
}

/* Left section: Videos */
.left {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-width: 30%; /* Ensures videos fit within the left side */
}

.video-container video {
  width: 100%;
  height: auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border: 1px solid #ccc;
}

/* Middle section: Images */
.middle {
  flex: 1;
  display: flex;
  color: green;
  flex-direction: column;
  gap: 10px;
  max-width: 30%; /* Ensures images fit within the middle section */
}

.image-container img {
  width: 100%;
  height: auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  border: 1px solid #ccc;
}

/* Right section: Typing text */
.right {
  flex: 1;
  max-width: 30%; /* Ensures text fits within the right side */
  font-size: 20px;
  white-space: pre-line;
}

/* Title with breathing flash effect */
.title {
  font-size: 25px;
  font-weight: bold;
  color: #8DC21F;
  text-align: center;
  margin-bottom: 10px;
}

.breathing-flash {
  animation: flash 1.5s ease-in-out infinite;
}

/* Flash effect animation */
@keyframes flash {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
  100% {
    opacity: 1;
  }
}

/* Styling for text labels above videos and images */
p {
  font-size: 16px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 5px;
}

/* Common size for informational text */
.info-text {
  font-size: 16px;
  font-weight: normal;
  text-align: left;
  margin-bottom: 10px;
}

/* Red text for '停车' */
.red-text {
  color: black;
  font-weight: bold;
}

/* Green text for '无车' */
.green-text {
  color: green;
  font-weight: bold;
}

/* Orange text for '占用' */
.orange-text {
  color: orange;
  font-weight: bold;
}
</style>
import * as tf from "@tensorflow/tfjs";
import * as posenet from "@tensorflow-models/posenet";

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

async function init() {
    const net = await posenet.load({
        inputResolution: { width: 640, height: 480 },
        scale: 0.8,
    });

    function processVideo() {
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        const tensor = tf.browser.fromPixels(canvas);
        net.estimateSinglePose(tensor).then(pose => {
            drawKeypoints(pose);
            tf.dispose(tensor);
        });
        requestAnimationFrame(processVideo);
    }

    requestAnimationFrame(processVideo);
}

function drawKeypoints(pose) {
    console.log('Pose detected:', pose);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    if (pose) {
        console.log('Keypoints:', pose.keypoints);
        for (const keypoint of pose.keypoints) {
            if (keypoint.score > 0.5) {
                console.log('Keypoint:', keypoint);
                ctx.beginPath();
                ctx.arc(keypoint.position.x, keypoint.position.y, 5, 0, 2 * Math.PI);
                ctx.fillStyle = 'green';
                ctx.fill();
            }
        }
    } else {
        console.log('No pose detected');
    }
}

init();

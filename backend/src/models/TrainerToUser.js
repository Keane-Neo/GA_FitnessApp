import mongoose from "mongoose";

// TO EDIT

const trainerToUserSchema = new mongoose.Schema({
  userDetailId: {
    type: String,
  },
  trainerId: {
    type: String,
  },
});

const TrainerToUser = mongoose.model("trainerToUser", trainerToUserSchema);

export default TrainerToUser;

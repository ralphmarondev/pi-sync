package com.ralphmarondev.pisync.features.home.domain.model

import com.google.gson.annotations.SerializedName

data class UserResponse(
    @SerializedName("success") val success: Boolean,
    @SerializedName("message") val message: String,
    @SerializedName("user") val user: User
)

data class User(
    @SerializedName("id") val id: Int,
    @SerializedName("registered_doors") val registeredDoors: List<Int>,
    @SerializedName("email") val email: String,
    @SerializedName("username") val username: String,
    @SerializedName("first_name") val firstName: String,
    @SerializedName("last_name") val lastName: String,
    @SerializedName("hint_password") val hintPassword: String,
    @SerializedName("is_superuser") val isSuperuser: Boolean,
    @SerializedName("gender") val gender: String,
    @SerializedName("create_date") val createDate: String,
    @SerializedName("created_by") val createdBy: String,
    @SerializedName("is_deleted") val isDeleted: Boolean,
    @SerializedName("update_date") val updateDate: String
)
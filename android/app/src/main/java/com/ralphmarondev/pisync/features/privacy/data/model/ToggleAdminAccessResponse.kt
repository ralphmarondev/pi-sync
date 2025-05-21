package com.ralphmarondev.pisync.features.privacy.data.model

import com.google.gson.annotations.SerializedName

data class ToggleAdminAccessResponse(
    val success: Boolean,
    val message: String,
    @SerializedName("allow_admin_access") val allowAdminAccess: Boolean
)

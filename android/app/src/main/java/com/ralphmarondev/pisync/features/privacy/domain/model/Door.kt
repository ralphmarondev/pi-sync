package com.ralphmarondev.pisync.features.privacy.domain.model

import com.google.gson.annotations.SerializedName

data class Door(
    val id: Int,
    val name: String,
    @SerializedName("is_active") val isActive: Boolean,
    @SerializedName("is_open") val isOpen: Boolean,
    @SerializedName("allow_admin_access") val allowAdminAccess: Boolean,
    @SerializedName("create_date") val createDate: String,
    @SerializedName("created_by") val createdBy: String,
    @SerializedName("is_deleted") val isDeleted: Boolean,
    @SerializedName("update_date") val updateDate: String,
    @SerializedName("tenant_count") val tenantCount: Int
)

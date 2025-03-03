package com.ralphmarondev.pisync.features.home.presentation.components

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.DarkMode
import androidx.compose.material.icons.outlined.LightMode
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeTopBar(
    darkTheme: Boolean,
    toggleDarkTheme: () -> Unit
) {
    TopAppBar(
        title = {
            Text(
                text = "Home",
            )
        },
        actions = {
            IconButton(onClick = toggleDarkTheme) {
                val icon =
                    if (darkTheme) Icons.Outlined.LightMode else Icons.Outlined.DarkMode
                Icon(
                    imageVector = icon,
                    contentDescription = "Theme Icon"
                )
            }
        },
        colors = TopAppBarDefaults.topAppBarColors(
            containerColor = MaterialTheme.colorScheme.primary,
            titleContentColor = MaterialTheme.colorScheme.onPrimary,
            actionIconContentColor = MaterialTheme.colorScheme.onPrimary
        )
    )
}
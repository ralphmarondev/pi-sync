package com.ralphmarondev.pisync.features.settings.presentation.overview.components

import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.DarkMode
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun ThemeToggleCard(
    modifier: Modifier = Modifier,
    darkTheme: Boolean,
    toggleDarkTheme: () -> Unit
) {
    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Icon(
            imageVector = Icons.Outlined.DarkMode,
            contentDescription = "Dark mode",
            tint = MaterialTheme.colorScheme.secondary
        )

        Spacer(modifier = Modifier.width(16.dp))
        Text(
            text = "Dark Mode",
            fontSize = 18.sp,
            fontWeight = FontWeight.W500,
            color = MaterialTheme.colorScheme.secondary
        )

        Spacer(modifier = Modifier.weight(1f))
        Switch(
            checked = darkTheme,
            onCheckedChange = { toggleDarkTheme() }
        )
    }
}
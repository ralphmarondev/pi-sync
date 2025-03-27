package com.ralphmarondev.pisync.features.history.presentation

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.DarkMode
import androidx.compose.material.icons.outlined.LightMode
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.ralphmarondev.pisync.core.util.LocalThemeState

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HistoryScreen() {
    val themeState = LocalThemeState.current

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "History"
                    )
                },
                actions = {
                    IconButton(
                        onClick = themeState::toggleTheme
                    ) {
                        val imageVector =
                            if (themeState.darkTheme.value) Icons.Outlined.LightMode else Icons.Outlined.DarkMode
                        Icon(
                            imageVector = imageVector,
                            contentDescription = "Theme toggle"
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
    ) { innerPadding ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
            contentAlignment = Alignment.Center
        ) {
            Text(
                text = "Hello there, Ralph Maron Eda is here!",
                fontWeight = MaterialTheme.typography.titleLarge.fontWeight,
                fontSize = MaterialTheme.typography.titleLarge.fontSize,
                color = MaterialTheme.colorScheme.secondary,
                modifier = Modifier.padding(16.dp),
                textAlign = TextAlign.Center
            )
        }
    }
}
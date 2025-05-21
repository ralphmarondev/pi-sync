package com.ralphmarondev.pisync.features.settings.presentation.overview

import androidx.compose.foundation.Image
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.outlined.Logout
import androidx.compose.material.icons.outlined.DarkMode
import androidx.compose.material.icons.outlined.Info
import androidx.compose.material.icons.outlined.LightMode
import androidx.compose.material.icons.outlined.PrivateConnectivity
import androidx.compose.material.icons.outlined.SettingsApplications
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
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
import androidx.compose.ui.draw.clip
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import coil.compose.rememberAsyncImagePainter
import com.ralphmarondev.pisync.R
import com.ralphmarondev.pisync.core.util.LocalThemeState
import com.ralphmarondev.pisync.features.settings.presentation.overview.components.SettingItemCard

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingScreen(
    logout: () -> Unit,
    navigateToAbout: () -> Unit,
    navigateToAppTheme: () -> Unit,
    navigateToPrivacy: () -> Unit
) {
    val themeState = LocalThemeState.current

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "Settings"
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
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            item {
                Spacer(modifier = Modifier.height(16.dp))
                Image(
                    painter = rememberAsyncImagePainter(R.drawable.app_icon),
                    contentDescription = "App icon",
                    contentScale = ContentScale.Crop,
                    modifier = Modifier
                        .size(120.dp)
                        .clip(CircleShape)
                )

                Spacer(modifier = Modifier.height(8.dp))
                Text(
                    text = stringResource(R.string.app_name),
                    fontWeight = FontWeight.W500,
                    fontSize = 20.sp,
                    textAlign = TextAlign.Center,
                    color = MaterialTheme.colorScheme.secondary
                )

                Text(
                    text = "Version 1.0",
                    fontWeight = FontWeight.W500,
                    fontSize = 14.sp,
                    textAlign = TextAlign.Center,
                    color = MaterialTheme.colorScheme.tertiary
                )
                HorizontalDivider(modifier = Modifier.padding(16.dp))
                SettingItemCard(
                    modifier = Modifier
                        .clickable { navigateToAbout() }
                        .fillMaxWidth()
                        .padding(16.dp),
                    label = "About",
                    imageVector = Icons.Outlined.Info
                )
                SettingItemCard(
                    modifier = Modifier
                        .clickable { navigateToAppTheme() }
                        .fillMaxWidth()
                        .padding(16.dp),
                    label = "App Theme",
                    imageVector = Icons.Outlined.SettingsApplications
                )
                SettingItemCard(
                    modifier = Modifier
                        .clickable { navigateToPrivacy() }
                        .fillMaxWidth()
                        .padding(16.dp),
                    label = "Privacy",
                    imageVector = Icons.Outlined.PrivateConnectivity
                )
                SettingItemCard(
                    modifier = Modifier
                        .clickable { logout() }
                        .fillMaxWidth()
                        .padding(16.dp),
                    label = "Logout",
                    imageVector = Icons.AutoMirrored.Outlined.Logout
                )
            }
        }
    }
}
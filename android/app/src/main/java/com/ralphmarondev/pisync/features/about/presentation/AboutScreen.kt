package com.ralphmarondev.pisync.features.about.presentation

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.ArrowBackIosNew
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedCard
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AboutScreen(
    navigateBack: () -> Unit
) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Text(
                        text = "About"
                    )
                },
                navigationIcon = {
                    IconButton(
                        onClick = navigateBack
                    ) {
                        Icon(
                            imageVector = Icons.Outlined.ArrowBackIosNew,
                            contentDescription = "Navigate back"
                        )
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primary,
                    titleContentColor = MaterialTheme.colorScheme.onPrimary,
                    navigationIconContentColor = MaterialTheme.colorScheme.onPrimary
                )
            )
        }
    ) { innerPadding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(innerPadding),
            contentPadding = PaddingValues(16.dp)
        ) {
            item {
                Text(
                    text = "Pi-Sync: Smarter Door Access",
                    fontSize = MaterialTheme.typography.titleMedium.fontSize,
                    fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                    color = MaterialTheme.colorScheme.primary
                )
                Text(
                    text = "Pi-Sync is a smart access system for condominiums, letting tenants open doors with their phones, fingerprint, or a backup key - all synced in real time.",
                    fontSize = MaterialTheme.typography.titleMedium.fontSize,
                    fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                    color = MaterialTheme.colorScheme.secondary
                )
                HorizontalDivider(modifier = Modifier.padding(vertical = 16.dp))
            }
            item {
                Text(
                    text = "Key Features",
                    fontSize = MaterialTheme.typography.titleMedium.fontSize,
                    fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                    color = MaterialTheme.colorScheme.primary
                )

                OutlinedCard(
                    modifier = Modifier
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Mobile Access",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Open doors using this app.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }

                OutlinedCard(
                    modifier = Modifier
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Fingerprint Login",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Fast, secure entry.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }

                OutlinedCard(
                    modifier = Modifier
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Real-Time Sync",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Always up to date, no need to wait.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }

                OutlinedCard(
                    modifier = Modifier
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Activity History",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "See when and where you accessed doors.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }
                HorizontalDivider(modifier = Modifier.padding(vertical = 16.dp))
            }

            item {
                Text(
                    text = "How It Works",
                    fontSize = MaterialTheme.typography.titleMedium.fontSize,
                    fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                    color = MaterialTheme.colorScheme.primary
                )

                OutlinedCard(
                    modifier = Modifier
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "This app connects with our building's smart access system through a secure server. It works alongside fingerprint sensors and a desktop dashboard used by admin staff. Everything syncs instantly to make sure access is smooth and secure.",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                    }
                }
                HorizontalDivider(modifier = Modifier.padding(vertical = 16.dp))
            }

            item {
                Text(
                    text = "Meet the Team",
                    fontSize = MaterialTheme.typography.titleMedium.fontSize,
                    fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                    color = MaterialTheme.colorScheme.primary
                )

                OutlinedCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Ralph Maron Eda",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Led the software development — from UI and app architecture to integration with hardware and server. Also contributed to the thesis documentation and overall project planning.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }


                OutlinedCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Jack Cabigayan",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Worked on documentation, data gathering, and supported the implementation of the system across different stages of development.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }

                OutlinedCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Triesha Mae Olunan",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Worked on documentation, data gathering, and supported the implementation of the system across different stages of development.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }

                OutlinedCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Jezlyn Cabbab",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Worked on documentation, data gathering, and supported the implementation of the system across different stages of development.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }
                HorizontalDivider(modifier = Modifier.padding(vertical = 16.dp))
            }

            item {
                Text(
                    text = "Thesis Adviser",
                    fontSize = MaterialTheme.typography.titleMedium.fontSize,
                    fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                    color = MaterialTheme.colorScheme.primary
                )
                OutlinedCard(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(vertical = 4.dp)
                ) {
                    Column(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(16.dp)
                    ) {
                        Text(
                            text = "Engr. Jerome Paul Viador",
                            fontSize = MaterialTheme.typography.titleMedium.fontSize,
                            fontWeight = MaterialTheme.typography.titleMedium.fontWeight,
                            color = MaterialTheme.colorScheme.secondary
                        )
                        Text(
                            text = "Guided us throughout the research and development process with valuable feedback and support.",
                            fontSize = MaterialTheme.typography.titleSmall.fontSize,
                            fontWeight = MaterialTheme.typography.titleSmall.fontWeight,
                            color = MaterialTheme.colorScheme.tertiary
                        )
                    }
                }
            }
            item {
                Spacer(modifier = Modifier.height(100.dp))
            }
        }
    }
}
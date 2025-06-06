﻿namespace PiSync.Tenant.NewTenant
{
    partial class NewTenantForm
    {
        /// <summary>
        /// Required designer variable.
        /// </>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            label10 = new Label();
            tbEmail = new TextBox();
            tbGender = new ComboBox();
            tbFingerprint = new ComboBox();
            btnSave = new Button();
            btnCancel = new Button();
            label7 = new Label();
            label8 = new Label();
            tbRegisteredDoors = new TextBox();
            label5 = new Label();
            tbPasswordHint = new TextBox();
            label6 = new Label();
            tbPassword = new TextBox();
            label3 = new Label();
            label4 = new Label();
            tbUsername = new TextBox();
            label2 = new Label();
            tbLastName = new TextBox();
            label1 = new Label();
            tbFirstName = new TextBox();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.Control;
            panel1.Controls.Add(label10);
            panel1.Controls.Add(tbEmail);
            panel1.Controls.Add(tbGender);
            panel1.Controls.Add(tbFingerprint);
            panel1.Controls.Add(btnSave);
            panel1.Controls.Add(btnCancel);
            panel1.Controls.Add(label7);
            panel1.Controls.Add(label8);
            panel1.Controls.Add(tbRegisteredDoors);
            panel1.Controls.Add(label5);
            panel1.Controls.Add(tbPasswordHint);
            panel1.Controls.Add(label6);
            panel1.Controls.Add(tbPassword);
            panel1.Controls.Add(label3);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(tbUsername);
            panel1.Controls.Add(label2);
            panel1.Controls.Add(tbLastName);
            panel1.Controls.Add(label1);
            panel1.Controls.Add(tbFirstName);
            panel1.Location = new Point(42, 25);
            panel1.Name = "panel1";
            panel1.Size = new Size(694, 551);
            panel1.TabIndex = 1;
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Font = new Font("Courier New", 11F);
            label10.Location = new Point(41, 158);
            label10.Name = "label10";
            label10.Size = new Size(76, 21);
            label10.TabIndex = 27;
            label10.Text = "Email:";
            // 
            // tbEmail
            // 
            tbEmail.Location = new Point(41, 185);
            tbEmail.Name = "tbEmail";
            tbEmail.PlaceholderText = "Enter email";
            tbEmail.Size = new Size(606, 30);
            tbEmail.TabIndex = 5;
            tbEmail.TabStop = false;
            // 
            // tbGender
            // 
            tbGender.DropDownStyle = ComboBoxStyle.DropDownList;
            tbGender.FormattingEnabled = true;
            tbGender.Items.AddRange(new object[] { "Male", "Female" });
            tbGender.Location = new Point(358, 116);
            tbGender.Name = "tbGender";
            tbGender.Size = new Size(289, 30);
            tbGender.TabIndex = 4;
            // 
            // tbFingerprint
            // 
            tbFingerprint.DropDownStyle = ComboBoxStyle.DropDownList;
            tbFingerprint.FormattingEnabled = true;
            tbFingerprint.Location = new Point(41, 417);
            tbFingerprint.Name = "tbFingerprint";
            tbFingerprint.Size = new Size(606, 30);
            tbFingerprint.TabIndex = 9;
            // 
            // btnSave
            // 
            btnSave.BackColor = Color.FromArgb(192, 255, 192);
            btnSave.Cursor = Cursors.Hand;
            btnSave.Location = new Point(197, 488);
            btnSave.Name = "btnSave";
            btnSave.Size = new Size(133, 47);
            btnSave.TabIndex = 10;
            btnSave.Text = "SAVE";
            btnSave.UseVisualStyleBackColor = false;
            btnSave.Click += btnSave_Click;
            // 
            // btnCancel
            // 
            btnCancel.BackColor = Color.FromArgb(255, 224, 192);
            btnCancel.Cursor = Cursors.Hand;
            btnCancel.Location = new Point(41, 488);
            btnCancel.Name = "btnCancel";
            btnCancel.Size = new Size(133, 47);
            btnCancel.TabIndex = 11;
            btnCancel.Text = "CANCEL";
            btnCancel.UseVisualStyleBackColor = false;
            btnCancel.Click += btnCancel_Click;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Courier New", 11F);
            label7.Location = new Point(41, 393);
            label7.Name = "label7";
            label7.Size = new Size(142, 21);
            label7.TabIndex = 19;
            label7.Text = "Fingerprint:";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Courier New", 11F);
            label8.Location = new Point(41, 314);
            label8.Name = "label8";
            label8.Size = new Size(197, 21);
            label8.TabIndex = 17;
            label8.Text = "Registered Doors:";
            // 
            // tbRegisteredDoors
            // 
            tbRegisteredDoors.Location = new Point(41, 341);
            tbRegisteredDoors.Name = "tbRegisteredDoors";
            tbRegisteredDoors.PlaceholderText = "If more than 1, separate by comma. Ex. A14, A15";
            tbRegisteredDoors.Size = new Size(606, 30);
            tbRegisteredDoors.TabIndex = 8;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("Courier New", 11F);
            label5.Location = new Point(358, 232);
            label5.Name = "label5";
            label5.Size = new Size(164, 21);
            label5.TabIndex = 15;
            label5.Text = "Password Hint:";
            // 
            // tbPasswordHint
            // 
            tbPasswordHint.Location = new Point(358, 259);
            tbPasswordHint.Name = "tbPasswordHint";
            tbPasswordHint.PlaceholderText = "Optional";
            tbPasswordHint.Size = new Size(289, 30);
            tbPasswordHint.TabIndex = 7;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Courier New", 11F);
            label6.Location = new Point(41, 232);
            label6.Name = "label6";
            label6.Size = new Size(109, 21);
            label6.TabIndex = 13;
            label6.Text = "Password:";
            // 
            // tbPassword
            // 
            tbPassword.Location = new Point(41, 259);
            tbPassword.Name = "tbPassword";
            tbPassword.PlaceholderText = "Enter password";
            tbPassword.Size = new Size(289, 30);
            tbPassword.TabIndex = 6;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 11F);
            label3.Location = new Point(358, 89);
            label3.Name = "label3";
            label3.Size = new Size(87, 21);
            label3.TabIndex = 11;
            label3.Text = "Gender:";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Courier New", 11F);
            label4.Location = new Point(41, 89);
            label4.Name = "label4";
            label4.Size = new Size(109, 21);
            label4.TabIndex = 9;
            label4.Text = "Username:";
            // 
            // tbUsername
            // 
            tbUsername.Location = new Point(41, 116);
            tbUsername.Name = "tbUsername";
            tbUsername.PlaceholderText = "Enter username";
            tbUsername.Size = new Size(289, 30);
            tbUsername.TabIndex = 3;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 11F);
            label2.Location = new Point(358, 15);
            label2.Name = "label2";
            label2.Size = new Size(120, 21);
            label2.TabIndex = 7;
            label2.Text = "Last Name:";
            // 
            // tbLastName
            // 
            tbLastName.Location = new Point(358, 42);
            tbLastName.Name = "tbLastName";
            tbLastName.PlaceholderText = "Enter last name";
            tbLastName.Size = new Size(289, 30);
            tbLastName.TabIndex = 2;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Courier New", 11F);
            label1.Location = new Point(41, 15);
            label1.Name = "label1";
            label1.Size = new Size(131, 21);
            label1.TabIndex = 5;
            label1.Text = "First Name:";
            // 
            // tbFirstName
            // 
            tbFirstName.Location = new Point(41, 42);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.PlaceholderText = "Enter first name";
            tbFirstName.Size = new Size(289, 30);
            tbFirstName.TabIndex = 1;
            // 
            // NewTenantForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(779, 598);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Margin = new Padding(4, 3, 4, 3);
            Name = "NewTenantForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "NEW TENANT";
            Load += NewTenantForm_Load;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label label8;
        private TextBox tbRegisteredDoors;
        private Label label5;
        private TextBox tbPasswordHint;
        private Label label6;
        private TextBox tbPassword;
        private Label label3;
        private Label label4;
        private TextBox tbUsername;
        private Label label2;
        private TextBox tbLastName;
        private Label label1;
        private TextBox tbFirstName;
        private Label label7;
        private Button btnSave;
        private Button btnCancel;
        private ComboBox tbFingerprint;
        private ComboBox tbGender;
        private Label label10;
        private TextBox tbEmail;
    }
}